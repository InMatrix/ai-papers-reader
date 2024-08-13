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

def get_summary_path(pdf_url):
    """
    Get the path to the summary file for a given PDF URL.

    Args:
    pdf_url (str): The URL of the PDF file.

    Returns:
    str: The path to the summary file.
    """
    paper_id = pdf_url.split('/')[-1]
    return f"docs/summaries/{paper_id}.md"

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
    response = model.generate_content([prompt, uploaded_file])
    
    # Clean up the temporary file
    os.unlink(temp_pdf.name)
    
    return response.text

def save_summary(summary, output_file):
    """
    Save the summary to a file.

    Args:
    summary (str): The summary to save.
    output_file (str): The path to the output file.
    """
    with open(output_file, 'w') as f:
        f.write(summary)

def main(pdf_url):
    """
    Main function to orchestrate the PDF download and summarization process.

    Args:
    pdf_url (str): The URL of the PDF to summarize.
    """
    summary_path = get_summary_path(pdf_url)
    if os.path.exists(summary_path):
        print(f"Summary for {pdf_url} already exists at {summary_path}")
        return summary_path
    
    print(f">>> Downloading PDF from {pdf_url}...")
    pdf_content = download_pdf(pdf_url)
    
    print(">>> Generating summary...")
    summary = summarize_pdf(pdf_content)
    
    print("\n>>> Summary:")
    print(summary)

    print(f"\n>>> Saving summary to {summary_path}")
    save_summary(summary, summary_path)
    return summary_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize a PDF from a given URL using Gemini 1.5 Flash.")
    parser.add_argument("url", help="The URL of the PDF to summarize")
    args = parser.parse_args()

    main(args.url)