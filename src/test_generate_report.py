import pytest
from generate_report import inflate_prompt, generate_report
import yaml
import shutil
from unittest.mock import Mock, patch
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
    shutil.copy(original_topics_path, topics_path)

    return prompt_template_path, paper_data_path, topics_path

def test_inflate_prompt(setup_files):
    prompt_template_path, paper_data_path, topics_path = setup_files

    # Read the topics from the copied _topics.yaml file
    with open(topics_path, 'r') as file:
        topics = yaml.safe_load(file)
        
    # Flatten the topics content into a single string
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

def test_generate_report_saves_partial_on_error(tmp_path):
    # Setup
    report_path = tmp_path / "report.md"
    date_string = "2023-10-27"

    mock_model = Mock()
    mock_model.generate_content.return_value = MockModelResponse(json.dumps(mock_json_response))

    prompt = "dummy prompt"
    topics = [{"topic": "Topic 1", "description": "Desc 1"}]

    # Mock add_summary_to_response to raise exception
    with patch('generate_report.add_summary_to_response') as mock_add_summary:
        mock_add_summary.side_effect = Exception("Quota exceeded")

        # Run generate_report
        # It should handle exception and print error, but not crash
        generate_report(mock_model, prompt, topics, date_string, str(report_path))

        # Verify
        assert report_path.exists()
        content = report_path.read_text()
        assert "Paper 1" in content
        assert "http://paper1.pdf" in content

        # Also check that we see the "Full paper" link
        assert "📄 **[Full paper](http://paper1.pdf)**" in content

def test_generate_report_saves_initial_before_summary(tmp_path):
    # Setup
    report_path = tmp_path / "report_initial.md"
    date_string = "2023-10-27"

    mock_model = Mock()
    mock_model.generate_content.return_value = MockModelResponse(json.dumps(mock_json_response))

    prompt = "dummy prompt"
    topics = [{"topic": "Topic 1", "description": "Desc 1"}]

    with patch('generate_report.add_summary_to_response') as mock_add_summary:
        mock_add_summary.return_value = mock_json_response # return same json
        with patch('generate_report.assess_relevance') as mock_assess:
            mock_assess.return_value = mock_json_response
            with patch('generate_report.write_summary_files'):

                generate_report(mock_model, prompt, topics, date_string, str(report_path))

                assert report_path.exists()
                content = report_path.read_text()
                assert "Paper 1" in content
