import pytest
from generate_report import inflate_prompt
import yaml
import shutil

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
    generated_prompt = inflate_prompt(str(prompt_template_path), str(paper_data_path), str(topics_path))

    assert generated_prompt == expected_prompt
