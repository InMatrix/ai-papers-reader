import json
import argparse
from typing import Dict, List, Any

def json_to_markdown(data: List[Dict[str, Any]], date: str) -> str:
    markdown = f"# {date}\n\n"
    
    for item in data:
        topic = item['topic']
        markdown += f"## {topic}\n\n"
        if not item['papers']:
            markdown += "No paper recommendations for this topic.\n\n"
        
        for paper in item['papers']:
            title = paper['title']
            relevance = paper['relevance']
            url = paper['url']
            
            markdown += f"### {title}\n\n"
            markdown += f"**Relevance:** {relevance}\n\n"
            
            if 'summary_path' in paper:
                summary_path = paper['summary_path'].replace('.md', '/')
                markdown += f"💡 **[Summary]({summary_path})** 📄 **[Full paper]({url})**\n\n"
            else:
                markdown += f"📄 **[Full paper]({url})**\n\n"
    
    return markdown

def convert_file(input_file: str, output_file: str) -> None:
    date: str = input_file.split('_')[-1].split('.')[0]

    with open(input_file, 'r') as f:
        data = json.load(f)
    
    markdown = json_to_markdown(data, date)
    
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