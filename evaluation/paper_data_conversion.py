# Convert a paper metadata file to a JSON array:

import json
import re

def extract_id(pdf_url):
    return pdf_url.split('/')[-1]

def parse_paper_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    papers = content.split('---')
    paper_data = []

    for paper in papers:
        if paper.strip():
            title_match = re.search(r'Title: (.+)', paper)
            pdf_match = re.search(r'PDF: (.+)', paper)
            summary_match = re.search(r'Summary: (.+)', paper, re.DOTALL)

            if title_match and pdf_match and summary_match:
                title = title_match.group(1).strip()
                pdf_url = pdf_match.group(1).strip()
                summary = summary_match.group(1).strip()

                paper_data.append({
                    "title": title,
                    "id": extract_id(pdf_url),
                    "summary": summary
                })

    return paper_data

def main():
    input_file = 'paper_data/paper_metadata_2024-09-20.txt'
    output_file = 'evaluation/paper_metadata_2024-09-20.json'

    paper_data = parse_paper_data(input_file)

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(paper_data, json_file, indent=2, ensure_ascii=False)

    print(f"Conversion complete. JSON data saved to {output_file}")

if __name__ == "__main__":
    main()