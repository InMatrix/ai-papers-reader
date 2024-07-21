import os
import argparse
import google.generativeai as genai

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def generate_report(model, paper_data, prompt_template, date_string):
    prompt = prompt_template.replace("{paper_data}", paper_data)
    response = model.generate_content(prompt)
    text_with_date = f"## {date_string}\n\n{response.text}"
    return text_with_date

def extract_date_from_paper_data_path(paper_data_path):
    return paper_data_path.split('_')[-1].split('.')[0]

def setup_argparse():
    parser = argparse.ArgumentParser(description='Generate a paper report using Gemini')
    parser.add_argument('--paper_data_path', default='paper_data/paper_metadata.txt', help='Path to paper data file')
    parser.add_argument('--report_path', default='docs/report_latest.md', help='Path to output report file')
    return parser.parse_args()

def main():
    args = setup_argparse()
    prompt_template_path = 'prompts/identify_papers.txt'
    
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY environment variable is not set")
    
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    paper_data = read_file(args.paper_data_path)
    date_string = extract_date_from_paper_data_path(args.paper_data_path)
    prompt_template = read_file(prompt_template_path)
    
    report_content = generate_report(model, paper_data, prompt_template, date_string)
    
    write_file(args.report_path, report_content)
    print(f"Report generated and saved to {args.report_path}")

if __name__ == "__main__":
    main()