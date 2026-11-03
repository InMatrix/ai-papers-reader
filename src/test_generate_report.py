import pytest
import generate_report as generate_report_module
from generate_report import inflate_prompt, generate_report
import yaml
import shutil
from unittest.mock import Mock, call, patch, MagicMock
import json
import os

@pytest.fixture
def setup_files(tmp_path):
    prompt_template_path = tmp_path / "prompt_template.txt"
    paper_data_path = tmp_path / "paper_data.txt"
    topics_path = tmp_path / "_topics.yaml"

    prompt_template_content = "This is a prompt template with {paper_data} and {topics}."
    paper_data_content = "Sample paper data."

    prompt_template_path.write_text(prompt_template_content)
    paper_data_path.write_text(paper_data_content)

    # Copy the _topics.yaml file to the temporary directory
    original_topics_path = "prompts/_topics.yaml"
    if os.path.exists(original_topics_path):
        shutil.copy(original_topics_path, topics_path)
    else:
        # Create a dummy topic file if original doesn't exist (e.g. running from different dir)
        with open(topics_path, 'w') as f:
            yaml.dump([{"topic": "Topic 1", "description": "Desc 1"}], f)

    return prompt_template_path, paper_data_path, topics_path

def test_inflate_prompt(setup_files):
    prompt_template_path, paper_data_path, topics_path = setup_files

    # Read the topics
    with open(topics_path, 'r') as file:
        topics = yaml.safe_load(file)
        
    topics_string = "\n".join([f"{index + 1}. {topic['topic']}\n{topic['description']}" for index, topic in enumerate(topics)])

    expected_prompt = f"This is a prompt template with Sample paper data. and {topics_string}."
    generated_prompt, _ = inflate_prompt(str(prompt_template_path), str(paper_data_path), str(topics_path))

    assert generated_prompt == expected_prompt

# Mock response from Gemini
mock_json_response = [
    {
        "topic": "Topic 1",
        "papers": [
            {
                "title": "Paper 1",
                "relevance": "High",
                "url": "http://paper1.pdf"
            }
        ]
    }
]

class MockModelResponse:
    def __init__(self, text):
        self.text = text

def test_generate_report_incremental(tmp_path):
    # Setup
    report_path = tmp_path / "report.md"
    paper_data_path = tmp_path / "paper_data.txt"
    date_string = "2023-10-27"

    # Create mock client with models attribute
    mock_client = Mock()
    mock_client.models.generate_content.return_value = MockModelResponse(json.dumps(mock_json_response))

    prompt = "dummy prompt"
    topics = [{"topic": "Topic 1", "description": "Desc 1"}]

    with patch('generate_report.summarize_pdf.pdf_to_summary') as mock_pdf_to_summary, \
         patch('generate_report.summarize_pdf.get_summary_path') as mock_get_path, \
         patch('generate_report.write_file') as mock_write_file, \
         patch('builtins.open', new_callable=MagicMock) as mock_open, \
         patch('generate_report.is_relevant') as mock_is_relevant, \
         patch('generate_report.update_status') as mock_update_status:

        mock_get_path.return_value = str(tmp_path / "summary.md")
        mock_pdf_to_summary.return_value = "Summary Content"
        mock_is_relevant.return_value = 0.9

        generate_report(mock_client, prompt, topics, str(paper_data_path), date_string, str(report_path))

        # Verify
        # 1. Summary generated
        mock_pdf_to_summary.assert_called()
        # 2. Report saved multiple times (Initial + After Paper 1)
        assert mock_write_file.call_count >= 2
        # 3. Summary written to file
        mock_open.assert_any_call(str(tmp_path / "summary.md"), 'w')
        # 4. Relevance checked
        mock_is_relevant.assert_called()
        # 5. Status updated
        assert mock_update_status.call_count >= 3 # initial, per paper, final

def test_generate_report_deletes_irrelevant(tmp_path):
    # Setup
    report_path = tmp_path / "report.md"
    paper_data_path = tmp_path / "paper_data.txt"
    date_string = "2023-10-27"
    summary_path = tmp_path / "summary.md"

    # Create mock client with models attribute
    mock_client = Mock()
    # 1. Recommendation
    mock_client.models.generate_content.return_value = MockModelResponse(json.dumps(mock_json_response))

    prompt = "dummy prompt"
    topics = [{"topic": "Topic 1", "description": "Desc 1"}]

    with patch('generate_report.summarize_pdf.pdf_to_summary') as mock_pdf_to_summary, \
         patch('generate_report.summarize_pdf.get_summary_path') as mock_get_path, \
         patch('generate_report.write_file') as mock_write_file, \
         patch('builtins.open', new_callable=MagicMock) as mock_open, \
         patch('os.remove') as mock_remove, \
         patch('generate_report.os.path.exists', return_value=True), \
         patch('generate_report.is_relevant') as mock_is_relevant, \
         patch('generate_report.update_status') as mock_update_status: # Mock only generate_report's view of os.path.exists

        mock_get_path.return_value = str(summary_path)
        mock_pdf_to_summary.return_value = "Summary Content"
        mock_is_relevant.return_value = 0.1

        generate_report(mock_client, prompt, topics, str(paper_data_path), date_string, str(report_path))

        # Verify deletion
        mock_remove.assert_called_with(str(summary_path))
        # Status should still be updated
        assert mock_update_status.called

def test_generate_report_saves_partial_on_error(tmp_path):
    # Setup
    report_path = tmp_path / "report.md"
    paper_data_path = tmp_path / "paper_data.txt"
    date_string = "2023-10-27"

    # Create mock client with models attribute
    mock_client = Mock()
    mock_client.models.generate_content.return_value = MockModelResponse(json.dumps(mock_json_response))

    prompt = "dummy prompt"
    topics = [{"topic": "Topic 1", "description": "Desc 1"}]

    # Mock summarize_pdf to raise exception
    with patch('generate_report.summarize_pdf.pdf_to_summary') as mock_pdf_to_summary, \
         patch('generate_report.summarize_pdf.get_summary_path') as mock_get_path, \
         patch('generate_report.update_status') as mock_update_status:

        mock_get_path.return_value = str(tmp_path / "summary.md")
        mock_pdf_to_summary.side_effect = Exception("Quota exceeded")

        # The failure is raised once the rest of the report has been saved
        with pytest.raises(RuntimeError, match=r"Could not summarize 1 paper\(s\): Paper 1"):
            generate_report(mock_client, prompt, topics, str(paper_data_path), date_string, str(report_path))

        # Should still have saved initial report and potentially partial updates (though here it failed on first paper)
        assert report_path.exists()
        # Initial status update should have happened
        mock_update_status.assert_any_call(str(paper_data_path), {"initial_report_generated": True})
        # The report is not marked final, so the retrigger workflow redoes the week
        mock_update_status.assert_any_call(str(paper_data_path), {"final_report_generated": False})
        assert call(str(paper_data_path), {"final_report_generated": True}) not in mock_update_status.call_args_list

def test_generate_report_fails_when_summary_is_empty(tmp_path):
    report_path = tmp_path / "report.md"
    paper_data_path = tmp_path / "paper_data.txt"

    mock_client = Mock()
    mock_client.models.generate_content.return_value = MockModelResponse(json.dumps(mock_json_response))

    topics = [{"topic": "Topic 1", "description": "Desc 1"}]

    with patch('generate_report.summarize_pdf.pdf_to_summary', return_value=None), \
         patch('generate_report.summarize_pdf.get_summary_path', return_value=str(tmp_path / "summary.md")), \
         patch('generate_report.update_status'):

        with pytest.raises(RuntimeError, match="Could not summarize 1 paper"):
            generate_report(mock_client, "dummy prompt", topics, str(paper_data_path), "2023-10-27", str(report_path))

    assert report_path.exists()

def test_generate_report_fails_when_topic_description_is_missing(tmp_path):
    report_path = tmp_path / "report.md"
    paper_data_path = tmp_path / "paper_data.txt"

    mock_client = Mock()
    mock_client.models.generate_content.return_value = MockModelResponse(json.dumps(mock_json_response))

    # The model's topic name matches none of the configured topics
    topics = [{"topic": "Another Topic", "description": "Desc"}]

    with patch('generate_report.summarize_pdf.pdf_to_summary') as mock_pdf_to_summary, \
         patch('generate_report.update_status') as mock_update_status:

        with pytest.raises(RuntimeError, match=r"Could not summarize 1 paper\(s\): Paper 1"):
            generate_report(mock_client, "dummy prompt", topics, str(paper_data_path), "2023-10-27", str(report_path))

        mock_pdf_to_summary.assert_not_called()
        mock_update_status.assert_any_call(str(paper_data_path), {"final_report_generated": False})

    assert report_path.exists()

shared_paper = {
    "title": "Shared Paper",
    "relevance": "High",
    "url": "https://arxiv.org/pdf/2310.00001"
}

listed_under_both_topics = [
    {"topic": "Topic 1", "papers": [shared_paper]},
    {"topic": "Topic 2", "papers": [shared_paper]}
]

def run_report_on_real_files(tmp_path, monkeypatch, recommendations, relevance_scores):
    # Only the LLM and the PDF download are faked, so the summary files, the
    # report, and status.json are the real ones. Returns the summarizer's mock.
    monkeypatch.chdir(tmp_path)
    (tmp_path / "paper_data").mkdir()

    mock_client = Mock()
    mock_client.models.generate_content.return_value = MockModelResponse(json.dumps(recommendations))
    topics = [{"topic": item["topic"], "description": item["topic"]} for item in recommendations]

    with patch('generate_report.summarize_pdf.download_pdf', return_value=b"pdf"), \
         patch('generate_report.summarize_pdf.summarize_pdf', return_value="# Title\nSummary") as mock_summarize_pdf, \
         patch('generate_report.is_relevant', side_effect=relevance_scores):
        generate_report(
            mock_client,
            "dummy prompt",
            topics,
            "paper_data/paper_metadata_2023-10-27.txt",
            "2023-10-27",
            "docs/2023-10-27/index.md"
        )

    return mock_summarize_pdf

def report_section(tmp_path, topic):
    report = (tmp_path / "docs" / "2023-10-27" / "index.md").read_text()
    return report.split(f"\n## {topic}\n")[1].split("\n## ")[0]

def papers_summarized(tmp_path):
    status = json.loads((tmp_path / "paper_data" / "status.json").read_text())
    return status["paper_metadata_2023-10-27.txt"]["papers_summarized"]

@pytest.mark.parametrize(
    "relevance_scores, kept_topic, dropped_topic",
    [
        ([0.9, 0.1], "Topic 1", "Topic 2"),
        ([0.1, 0.9], "Topic 2", "Topic 1")
    ],
    ids=["keep_then_drop", "drop_then_keep"]
)
def test_generate_report_keeps_summary_shared_with_a_topic_that_kept_the_paper(
    tmp_path, monkeypatch, relevance_scores, kept_topic, dropped_topic
):
    mock_summarize_pdf = run_report_on_real_files(tmp_path, monkeypatch, listed_under_both_topics, relevance_scores)

    # The link under the topic that kept the paper points at a file that exists
    assert "[Summary](2310.00001/)" in report_section(tmp_path, kept_topic)
    assert (tmp_path / "docs" / "2023-10-27" / "2310.00001.md").exists()
    # The paper is still dropped from the other topic
    assert "Shared Paper" not in report_section(tmp_path, dropped_topic)
    assert papers_summarized(tmp_path) == {shared_paper["url"]: True}
    # The second topic reuses the summary instead of generating it again
    mock_summarize_pdf.assert_called_once()

def test_generate_report_deletes_summary_when_every_topic_dropped_the_paper(tmp_path, monkeypatch):
    mock_summarize_pdf = run_report_on_real_files(tmp_path, monkeypatch, listed_under_both_topics, [0.1, 0.2])

    assert not (tmp_path / "docs" / "2023-10-27" / "2310.00001.md").exists()
    assert papers_summarized(tmp_path) == {shared_paper["url"]: False}
    mock_summarize_pdf.assert_called_once()

def test_generate_report_deletes_dropped_summary_on_a_run_with_failures(tmp_path, monkeypatch):
    failing_paper = {
        "title": "Failing Paper",
        "relevance": "High",
        "url": "https://arxiv.org/pdf/2310.00002"
    }
    recommendations = [{"topic": "Topic 1", "papers": [shared_paper, failing_paper]}]

    with pytest.raises(RuntimeError, match=r"Could not summarize 1 paper\(s\): Failing Paper"):
        run_report_on_real_files(tmp_path, monkeypatch, recommendations, [0.1, Exception("Quota exceeded")])

    assert not (tmp_path / "docs" / "2023-10-27" / "2310.00001.md").exists()
    assert papers_summarized(tmp_path) == {shared_paper["url"]: False}

def test_report_api_spend_prints_and_writes_job_summary(tmp_path, monkeypatch, capsys):
    summary_path = tmp_path / "step_summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary_path))
    usage = "claude-haiku-5-5: 2 requests, 100,000 input and 3,000 output tokens, estimated cost $0.0115"

    with patch('generate_report.claude_usage_summary', return_value=[usage]):
        generate_report_module.report_api_spend("2023-10-27", "claude", "claude-haiku-5-5")

    line = f"API spend for the 2023-10-27 report: {usage}"
    assert line in capsys.readouterr().out
    assert summary_path.read_text() == f"{line}\n\n"

def test_report_api_spend_reports_a_claude_run_with_no_completed_requests(monkeypatch, capsys):
    monkeypatch.delenv("GITHUB_STEP_SUMMARY", raising=False)

    with patch('generate_report.claude_usage_summary', return_value=[]):
        generate_report_module.report_api_spend("2023-10-27", "claude", "claude-haiku-5-5")

    assert capsys.readouterr().out == (
        "API spend for the 2023-10-27 report: claude-haiku-5-5: no completed requests\n"
    )

@pytest.mark.parametrize("provider", ["gemini", "deepseek"])
def test_report_api_spend_is_silent_for_other_providers(provider, monkeypatch, capsys):
    monkeypatch.delenv("GITHUB_STEP_SUMMARY", raising=False)

    with patch('generate_report.claude_usage_summary', return_value=[]):
        generate_report_module.report_api_spend("2023-10-27", provider, "some-model")

    assert capsys.readouterr().out == ""
