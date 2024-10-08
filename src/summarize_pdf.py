"""
PDF Summarizer using Google's Gemini 1.5 Flash Model

This script downloads a PDF from a given URL and generates a summary using 
Google's Gemini 1.5 Flash model. It utilizes the google-generativeai library 
to interact with the Gemini model and directly uploads the PDF for processing.

Features:
- Downloads a PDF from a specified URL
- Uploads the PDF directly to the Gemini model using genai.upload_file
- Generates a 500-word summary of the PDF content
- Accepts the PDF URL as a command-line argument

Requirements:
- Python 3.7+
- google-generativeai library
- requests library

Usage:
1. Install required libraries:
   pip install google-generativeai requests

2. Set your Google API key in the script or as an environment variable:
   export GOOGLE_API_KEY='your_google_api_key_here'

3. Run the script with a PDF URL as an argument:
   python summarize_pdf.py https://arxiv.org/pdf/2407.16741

Note: Ensure you have the necessary permissions and comply with the terms of service 
for both the PDF source and the Google Generative AI API.
"""

import os
import argparse
import requests
import tempfile
import google.generativeai as genai

# Configure the generative AI model
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash')

def download_pdf(url):
    """
    Download a PDF file from the given URL.

    Args:
    url (str): The URL of the PDF file to download.

    Returns:
    bytes: The content of the PDF file.
    """
    response = requests.get(url)
    return response.content

def get_summary_path(pdf_url, save_location="docs/summaries"):
    """
    Get the path to the summary file for a given PDF URL.

    Args:
    pdf_url (str): The URL of the PDF file.
    save_location (str): Optional. The directory to save the summary file. Default is "docs/summaries".

    Returns:
    str: The path to the summary file.
    """
    # Create the folder of `save_location` if it doesn't exist
    os.makedirs(save_location, exist_ok=True)
    
    # Extract the paper ID from the URL
    paper_id = pdf_url.split('/')[-1]
    
    # Return the path to the summary file
    return f"{save_location}/{paper_id}.md"

def summarize_pdf(pdf_content):
    """
    Summarize the content of a PDF using the Gemini 1.5 Flash model.

    Args:
    pdf_content (bytes): The content of the PDF file.

    Returns:
    str: A 500-word summary of the PDF content.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
        temp_pdf.write(pdf_content)
        temp_pdf.flush()
        
        # Upload the PDF file
        uploaded_file = genai.upload_file(path=temp_pdf.name, display_name="paper.pdf")
        
    # Generate content using the uploaded file
    with open('prompts/summarize_paper.txt', 'r') as file:
        prompt = file.read().strip()
    
    try:
        response = model.generate_content([prompt, uploaded_file])
    except Exception as e:
        print(f"Error generating content: {e}")
        return None
    
    # Clean up the temporary file
    os.unlink(temp_pdf.name)
    
    return response.text

def add_front_matter(summary, summary_path):
        """
        Adds front matter to the summary.

        Args:
        summary (str): The summary to which front matter will be added.
        summary_path (str): The path of the summary file, used to generate the permalink.

        Returns:
        str: The summary with added front matter.
        """
        # Extract the title from the first line of the summary
        title_line = summary.split('\n', 1)[0]
        # Remove all the leading or trailing '#', '*' and whitespace
        title = title_line.strip('#* ')
        
        # Generate the permalink based on the summary file's path
        permalink = summary_path.replace(".md", ".html").replace("docs/","")
        
        front_matter = f"---\nlayout: default\ntitle: \'{title}\'\npermalink: {permalink}\n---\n"
        return front_matter + summary

def save_summary(summary, output_file):
    """
    Save the summary to a file.

    Args:
    summary (str): The summary to save.
    output_file (str): The path to the output file.
    """
    with open(output_file, 'w') as f:
        f.write(summary)

def main(pdf_url, save_location="docs/summaries"):
    """
    Main function to orchestrate the PDF download and summarization process.

    Args:
    pdf_url (str): The URL of the PDF to summarize.
    save_location (str): Optional. The directory to save the summary file. Default is "docs/summaries".
    """
    summary_path = get_summary_path(pdf_url, save_location)
    if os.path.exists(summary_path):
        print(f"Summary for {pdf_url} already exists at {summary_path}")
        return summary_path
    
    print(f">>> Downloading PDF from {pdf_url}...")
    pdf_content = download_pdf(pdf_url)
    
    print(">>> Generating summary...")
    summary = summarize_pdf(pdf_content)

    if summary is None:
        print(f"Failed to generate summary for {pdf_url}")
        return None

    # Add front matter to the summary
    print(">>> Adding front matter...")
    summary_with_front_matter = add_front_matter(summary, summary_path)

    print(f">>> Saving summary to {summary_path}\n")
    save_summary(summary_with_front_matter, summary_path)
    return summary_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize a PDF from a given URL using Gemini 1.5 Flash.")
    parser.add_argument("url", help="The URL of the PDF to summarize")
    parser.add_argument("--save_location", default="docs/summaries", help="Directory to save the summary file. Default is 'docs/summaries'.")
    args = parser.parse_args()

    main(args.url, args.save_location)