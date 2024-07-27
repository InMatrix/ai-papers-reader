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
        report_dir = 'docs'
        args.report_path = os.path.join(report_dir, f"report_{date_string}.md")
    
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