import pytest
from generate_report import inflate_prompt

@pytest.fixture
def setup_files(tmp_path):
    prompt_template_path = tmp_path / "prompt_template.txt"
    paper_data_path = tmp_path / "paper_data.txt"
    topics_path = tmp_path / "_topics.txt"

    prompt_template_content = "This is a prompt template with {paper_data} and {topics}."
    paper_data_content = "Sample paper data."
    topics_content = "Sample topics"

    prompt_template_path.write_text(prompt_template_content)
    paper_data_path.write_text(paper_data_content)
    topics_path.write_text(topics_content)

    return prompt_template_path, paper_data_path, topics_path

def test_inflate_prompt(setup_files):
    prompt_template_path, paper_data_path, topics_path = setup_files

    expected_prompt = "This is a prompt template with Sample paper data. and Sample topics."
    generated_prompt = inflate_prompt(str(prompt_template_path), str(paper_data_path), str(topics_path))

    assert generated_prompt == expected_prompt