import os
import argparse
import json
import yaml
import google.generativeai as genai
import summarize_pdf
from json_to_markdown import json_to_markdown


# Helper functions
def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def write_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)


def parse_model_response(response):
    try:
        # Remove leading and trailing whitespace and markdown code block markers
        cleaned_response = response.text.strip()
        if cleaned_response.startswith("```json") and cleaned_response.endswith("```"):
            cleaned_response = cleaned_response[7:-3].strip()
        # Remove newline characters
        cleaned_response = cleaned_response.replace("\n", "")
        # Parse the cleaned response as JSON
        response_json = json.loads(cleaned_response)
    except json.JSONDecodeError:
        # Print the response in json format
        print(json.dumps(cleaned_response, indent=4))
        raise ValueError("The response is not a valid JSON string")
    return response_json


def add_summary_to_response(response_json, save_location):
    """
    Iterate over the response json and add a summary
    for each paper based on its URL
    """
    for topic in response_json:
        for paper in topic["papers"]:
            summary_path = summarize_pdf.get_summary_path(paper["url"], save_location)
            summary_content = summarize_pdf.pdf_to_summary(paper["url"], summary_path)
            if summary_path is not None:
                # Use relative path to the summary file
                paper["summary_path"] = summary_path.replace(
                    f"{save_location}/", ""
                )
                paper["summary_content"] = summary_content
    return response_json

def assess_relevance(response_json, topics, model):
    """
    Assess the relevance of each paper's summary to its topic description
    and remove irrelevant papers.
    """
    dropped_papers = []
    for topic in response_json:
        topic_description = next((t['description'] for t in topics if t['topic'] == topic['topic']), None)
        if not topic_description:
            raise ValueError(f"Topic description not found for {topic['topic']}")
        
        relevant_papers = []
        for paper in topic["papers"]:
            summary_content = paper.get("summary_content", "")
            relevance_score = is_relevant(summary_content, topic_description, model)
            if relevance_score >= 0.5:
                relevant_papers.append(paper)
            else:
                dropped_papers.append({
                    "topic": topic['topic'],
                    "paper_title": paper.get("title", "Unknown Title"),
                    "relevance_score": relevance_score
                })
        
        topic["papers"] = relevant_papers
    
    # Print dropped papers
    for paper in dropped_papers:
        print(f"Dropped paper '{paper['paper_title']}' from topic '{paper['topic']}' with relevance score: {paper['relevance_score']}")
    
    return response_json

def is_relevant(summary, topic_description, model, threshold=0.5):
    """
    Check if the summary is relevant to the topic description using the AI model.
    """
    prompt = f"Is the following paper summary relevant to the topic description?\n\nSummary: {summary}\n\nTopic Description: {topic_description}\n\nAnswer with a relevance score between 0 and 1. No explanation is needed"
    response = model.generate_content(prompt)
    relevance_score = float(response.text.strip())
    return relevance_score

def write_summary_files(response_json, save_location):
    """
    Write the summary content to a file for each paper in the response json.
    """
    for topic in response_json:
        for paper in topic["papers"]:
            summary_path = paper.get("summary_path")
            summary_content = paper.get("summary_content")
            if summary_path is not None and summary_content is not None:
                # Write the summary content to a file
                with open(os.path.join(save_location, summary_path), "w") as file:
                    file.write(summary_content)
                # Print out which paper's summary has been saved to a file
                print(f"Saved a summary of the paper {paper['title']} to {summary_path}")

def inflate_prompt(
    prompt_template_path, paper_data_path, topics_path="prompts/_topics.yaml"
):
    """
    Generates a prompt by replacing placeholders in a template with actual data.

    Args:
        prompt_template_path (str): The file path to the prompt template.
        paper_data_path (str): The file path to the paper data.
        topics_path (str, optional): The file path to the topics data. Defaults to "prompts/_topics.yaml".

    Returns:
        str: The generated prompt with placeholders replaced by actual data.
    """
    prompt_template = read_file(prompt_template_path)
    paper_data = read_file(paper_data_path)
    
    # Read topics from YAML file
    with open(topics_path, 'r') as file:
        topics = yaml.safe_load(file)
    
    # Convert topics to a string format suitable for the prompt
    topics_str = "\n".join([f"{index + 1}. {topic['topic']}\n{topic['description']}" for index, topic in enumerate(topics)])
    
    prompt = prompt_template.replace("{paper_data}", paper_data).replace(
        "{topics}", topics_str
    )
    return prompt, topics


def generate_report(model, prompt, topics, date_string, skip_summary=False):
    # generate paper recommendations in json format
    response = model.generate_content(prompt)
    response_json = parse_model_response(response)
    
    if not skip_summary:
        # create paper summaries
        summary_save_location = os.path.join("docs", date_string)
        response_json = add_summary_to_response(
            response_json, save_location=summary_save_location
        )
        # assess relevance based on paper summaries and drop less relevant papers
        response_json = assess_relevance(response_json, topics, model)
        write_summary_files(response_json, summary_save_location)
    
    # convert json to markdown
    markdown_content = json_to_markdown(response_json, date_string)
    # add front matter to the markdown content
    markdown_content = f"---\nlayout: default\ntitle: {date_string}\npermalink: /{date_string}/\n---\n\n{markdown_content}"
    return markdown_content


def extract_date_from_paper_data_path(paper_data_path):
    return paper_data_path.split("_")[-1].split(".")[0]


def get_most_recent_file(directory):
    files = [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]
    if not files:
        raise FileNotFoundError(f"No files found in {directory}")
    return max(files, key=os.path.getctime)


def setup_argparse():
    parser = argparse.ArgumentParser(description="Generate paper report")
    parser.add_argument("--paper_data_path", help="Path to paper data file")
    parser.add_argument("--report_path", help="Path to output report file")
    parser.add_argument("--skip_summary", action="store_true", help="Skip the summarization step")
    return parser


def main():
    parser = setup_argparse()
    args = parser.parse_args()

    if args.paper_data_path is None:
        paper_data_dir = "paper_data"
        args.paper_data_path = get_most_recent_file(paper_data_dir)
        print(f"Using the most recent file: {args.paper_data_path}")

    date_string = extract_date_from_paper_data_path(args.paper_data_path)

    if args.report_path is None:
        report_dir = os.path.join("docs", date_string)
        os.makedirs(report_dir, exist_ok=True)  # Create the folder if it doesn't exist
        args.report_path = os.path.join(report_dir, "index.md")

    prompt_template_path = "prompts/recommend_papers.txt"

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY environment variable is not set")

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt, topics = inflate_prompt(prompt_template_path, args.paper_data_path)
    report_content = generate_report(model, prompt, topics, date_string, skip_summary=args.skip_summary)

    write_file(args.report_path, report_content)
    print(f"Report generated and saved to {args.report_path}")


if __name__ == "__main__":
    main()
