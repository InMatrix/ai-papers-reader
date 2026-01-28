import os
import argparse
import json
import yaml
import time
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
        # Remove leading and trailing whitespace
        cleaned_response = response.text.strip()
        
        # Remove markdown code fences if present
        # Handle ```json\n...\n``` format
        if cleaned_response.startswith("```json"):
            cleaned_response = cleaned_response[7:]  # Remove ```json
        # Handle ```\n...\n``` format
        elif cleaned_response.startswith("```"):
            cleaned_response = cleaned_response[3:]  # Remove ```
        
        # Remove trailing code fence
        if cleaned_response.endswith("```"):
            cleaned_response = cleaned_response[:-3]  # Remove ```
        
        # Remove any leading text before the JSON array/object starts
        # Find the first occurrence of [ or {
        start_idx = -1
        for i, char in enumerate(cleaned_response):
            if char in ['{', '[']:
                start_idx = i
                break
        
        if start_idx > 0:
            cleaned_response = cleaned_response[start_idx:]
        
        # Strip again after all processing
        cleaned_response = cleaned_response.strip()
        
        # Parse the cleaned response as JSON
        response_json = json.loads(cleaned_response)
    except json.JSONDecodeError as e:
        # Print detailed error information
        print(f"JSON decode error: {str(e)}")
        
        # Print context around error position
        error_pos = e.pos
        start = max(0, error_pos - 40)
        end = min(len(cleaned_response), error_pos + 40)
        print(f"Context: ...{cleaned_response[start:error_pos]}>>>ERROR HERE>>>{cleaned_response[error_pos:end]}...")
        
        # Save the problematic response to a file for inspection
        debug_file = "error_response.txt"
        with open(debug_file, "w") as f:
            f.write(cleaned_response)
        print(f"Full response saved to '{debug_file}' for inspection")
        
        raise ValueError(f"The response is not a valid JSON string: {str(e)}")
    
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
    prompt = f"""Is the following paper summary relevant to the topic description?

Summary: {summary}

Topic Description: {topic_description}

Answer with ONLY a single number between 0 and 1 representing the relevance score. 
Do not include any other text, explanation, or JSON formatting. 
Just output the number, for example: 0.9"""
    
    response = model.generate_content(prompt)
    # The Gemini free tier has a rate limit of 15 RPM
    time.sleep(5)
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


def generate_report(model, prompt, topics, date_string, report_path, skip_summary=False):
    # generate paper recommendations in json format
    response = model.generate_content(prompt)
    response_json = parse_model_response(response)
    
    # helper to generate and save markdown
    def save_markdown(data):
        content = json_to_markdown(data, date_string)
        content = f"---\nlayout: default\ntitle: {date_string}\npermalink: /{date_string}/\n---\n\n{content}"
        write_file(report_path, content)
        return content

    # Save initial report
    markdown_content = save_markdown(response_json)
    
    if not skip_summary:
        try:
            # create paper summaries
            summary_save_location = os.path.join("docs", date_string)
            response_json = add_summary_to_response(
                response_json, save_location=summary_save_location
            )
            # assess relevance based on paper summaries and drop less relevant papers
            response_json = assess_relevance(response_json, topics, model)
            write_summary_files(response_json, summary_save_location)

            # Update report with summaries
            markdown_content = save_markdown(response_json)
        except Exception as e:
            print(f"Error during summarization: {e}")
            print("Saving partial progress...")
            markdown_content = save_markdown(response_json)

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
    return max(files, key=os.path.getmtime)


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
    
    # Configure the model with JSON response format
    generation_config = {
        "response_mime_type": "application/json",
        "temperature": 0.7,
    }
    model = genai.GenerativeModel("gemini-flash-latest", generation_config=generation_config)

    prompt, topics = inflate_prompt(prompt_template_path, args.paper_data_path)
    generate_report(model, prompt, topics, date_string, args.report_path, skip_summary=args.skip_summary)

    print(f"Report generated and saved to {args.report_path}")


if __name__ == "__main__":
    """
    Command-line Usage:

    python generate_report.py [OPTIONS]

    Options:
      --paper_data_path PATH   Path to the paper data file. If not provided, the most recent file in the 'paper_data' directory will be used.
      --report_path PATH       Path to save the generated report. If not provided, the report will be saved in 'docs/<date_string>/index.md'.
      --skip_summary           Skip the summarization step. Use this flag to bypass generating summaries for papers.

    Examples:
      1. Generate a report using the most recent paper data file and default settings:
         python generate_report.py

      2. Generate a report for a specific paper data file:
         python generate_report.py --paper_data_path paper_data/sample_papers_20231001.json

      3. Generate a report and save it to a specific location:
         python generate_report.py --paper_data_path paper_data/sample_papers_20231001.json --report_path docs/custom_report.md

      4. Generate a report without summarizing papers:
         python generate_report.py --skip_summary
    """
    main()
