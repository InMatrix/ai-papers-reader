import pytest
from generate_report import inflate_prompt, generate_report
import yaml
import shutil
from unittest.mock import Mock, patch, MagicMock
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
    date_string = "2023-10-27"

    mock_model = Mock()
    # Mock responses for generate_report
    # 1. Recommendation (response_json)
    mock_model.generate_content.return_value = MockModelResponse(json.dumps(mock_json_response))

    prompt = "dummy prompt"
    topics = [{"topic": "Topic 1", "description": "Desc 1"}]

    with patch('generate_report.summarize_pdf.pdf_to_summary') as mock_pdf_to_summary, \
         patch('generate_report.summarize_pdf.get_summary_path') as mock_get_path, \
         patch('generate_report.write_file') as mock_write_file, \
         patch('builtins.open', new_callable=MagicMock) as mock_open, \
         patch('generate_report.is_relevant') as mock_is_relevant:

        mock_get_path.return_value = str(tmp_path / "summary.md")
        mock_pdf_to_summary.return_value = "Summary Content"
        mock_is_relevant.return_value = 0.9

        generate_report(mock_model, prompt, topics, date_string, str(report_path))

        # Verify
        # 1. Summary generated
        mock_pdf_to_summary.assert_called()
        # 2. Report saved multiple times (Initial + After Paper 1)
        assert mock_write_file.call_count >= 2
        # 3. Summary written to file
        mock_open.assert_any_call(str(tmp_path / "summary.md"), 'w')
        # 4. Relevance checked
        mock_is_relevant.assert_called()

def test_generate_report_deletes_irrelevant(tmp_path):
    # Setup
    report_path = tmp_path / "report.md"
    date_string = "2023-10-27"
    summary_path = tmp_path / "summary.md"

    mock_model = Mock()
    # 1. Recommendation
    mock_model.generate_content.return_value = MockModelResponse(json.dumps(mock_json_response))

    prompt = "dummy prompt"
    topics = [{"topic": "Topic 1", "description": "Desc 1"}]

    with patch('generate_report.summarize_pdf.pdf_to_summary') as mock_pdf_to_summary, \
         patch('generate_report.summarize_pdf.get_summary_path') as mock_get_path, \
         patch('generate_report.write_file') as mock_write_file, \
         patch('builtins.open', new_callable=MagicMock) as mock_open, \
         patch('os.remove') as mock_remove, \
         patch('generate_report.os.path.exists', return_value=True), \
         patch('generate_report.is_relevant') as mock_is_relevant: # Mock only generate_report's view of os.path.exists

        mock_get_path.return_value = str(summary_path)
        mock_pdf_to_summary.return_value = "Summary Content"
        mock_is_relevant.return_value = 0.1

        generate_report(mock_model, prompt, topics, date_string, str(report_path))

        # Verify deletion
        mock_remove.assert_called_with(str(summary_path))

def test_generate_report_saves_partial_on_error(tmp_path):
    # Setup
    report_path = tmp_path / "report.md"
    date_string = "2023-10-27"

    mock_model = Mock()
    mock_model.generate_content.return_value = MockModelResponse(json.dumps(mock_json_response))

    prompt = "dummy prompt"
    topics = [{"topic": "Topic 1", "description": "Desc 1"}]

    # Mock summarize_pdf to raise exception
    with patch('generate_report.summarize_pdf.pdf_to_summary') as mock_pdf_to_summary, \
         patch('generate_report.summarize_pdf.get_summary_path') as mock_get_path:

        mock_get_path.return_value = str(tmp_path / "summary.md")
        mock_pdf_to_summary.side_effect = Exception("Quota exceeded")

        generate_report(mock_model, prompt, topics, date_string, str(report_path))

        # Should still have saved initial report and potentially partial updates (though here it failed on first paper)
        assert report_path.exists()
