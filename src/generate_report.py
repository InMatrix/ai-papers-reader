import os
import argparse
import json
import google.generativeai as genai
import summarize_pdf
from json_to_markdown import json_to_markdown 

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


def clean_model_response(response):
    """
    Clean up the response from the AI model 
    by removing the first and last lines.
    """
    # Split the string by newlines
    lines = response.text.splitlines()
    # Remove the first and last lines
    lines = lines[1:-1]
    # Join the remaining lines back into a string
    modified_response = "\n".join(lines)
    # Parse the modified response as JSON
    return json.loads(modified_response)

def add_summary_to_response(response_json, save_location):
    """
    Iterate over the response json and add a summary 
    for each paper based on its URL
    """
    for topic in response_json:
        for paper in topic['papers']:
            summary_path = summarize_pdf.main(paper['url'],save_location=save_location)
            # Use relative path to the summary file
            paper['summary'] = summary_path.replace(f'{save_location}/', '').replace('.md', '.html')
    return response_json

def generate_report(model, paper_data, prompt_template, date_string):
    prompt = prompt_template.replace("{paper_data}", paper_data)
    response = model.generate_content(prompt)
    response_json = clean_model_response(response)
    summary_save_location = os.path.join('docs', date_string)
    modified_response_json =add_summary_to_response(response_json, save_location=summary_save_location)
    markdown_content = json_to_markdown(modified_response_json, date_string)
    # add front matter to the markdown content
    markdown_content = f"---\nlayout: default\ntitle: {date_string}\npermalink: /{date_string}/\n---\n\n{markdown_content}"
    return markdown_content

def extract_date_from_paper_data_path(paper_data_path):
    return paper_data_path.split('_')[-1].split('.')[0]

def get_most_recent_file(directory):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:
        raise FileNotFoundError(f"No files found in {directory}")
    return max(files, key=os.path.getctime)

def setup_argparse():
    parser = argparse.ArgumentParser(description='Generate paper report')
    parser.add_argument('--paper_data_path', help='Path to paper data file')
    parser.add_argument('--report_path', help='Path to output report file')
    return parser

def main():
    parser = setup_argparse()
    args = parser.parse_args()

    if args.paper_data_path is None:
        paper_data_dir = 'paper_data'
        args.paper_data_path = get_most_recent_file(paper_data_dir)
        print(f"Using the most recent file: {args.paper_data_path}")

    date_string = extract_date_from_paper_data_path(args.paper_data_path)

    if args.report_path is None:
        report_dir = os.path.join('docs', date_string)
        os.makedirs(report_dir, exist_ok=True)  # Create the folder if it doesn't exist
        args.report_path = os.path.join(report_dir, 'index.md')
    
    prompt_template_path = 'prompts/identify_papers.txt'
    
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY environment variable is not set")
    
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    paper_data = read_file(args.paper_data_path)
    prompt_template = read_file(prompt_template_path)
    report_content = generate_report(model, paper_data, prompt_template, date_string)

    write_file(args.report_path, report_content)
    print(f"Report generated and saved to {args.report_path}")

if __name__ == "__main__":
    main()