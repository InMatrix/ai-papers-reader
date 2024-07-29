import json
import argparse
from typing import Dict, List, Any

def json_to_markdown(data: List[Dict[str, Any]]) -> str:
    markdown = "# Research Topics and Papers\n\n"
    
    for item in data:
        topic = item['topic']
        markdown += f"## {topic}\n\n"
        
        for paper in item['papers']:
            title = paper['title']
            relevance = paper['relevance']
            url = paper['url']
            summary = paper['summary']
            
            markdown += f"### [{title}]({url})\n\n"
            markdown += f"**Relevance:** {relevance}\n\n"
            markdown += f"**Summary:** [Link to summary]({summary})\n\n"
    
    return markdown

def convert_file(input_file: str, output_file: str) -> None:
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    markdown = json_to_markdown(data)
    
    with open(output_file, 'w') as f:
        f.write(markdown)
    
    print(f"Conversion complete. Markdown file saved as {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Convert JSON file to Markdown")
    parser.add_argument("input_file", help="Input JSON file")
    parser.add_argument("output_file", help="Output Markdown file")
    args = parser.parse_args()

    convert_file(args.input_file, args.output_file)

if __name__ == "__main__":
    main()