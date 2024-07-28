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
    prompt = "Write a 500-word blog post summarizing the paper in the attached PDF file."
    response = model.generate_content([prompt, uploaded_file])
    
    # Clean up the temporary file
    os.unlink(temp_pdf.name)
    
    return response.text

def main(pdf_url):
    """
    Main function to orchestrate the PDF download and summarization process.

    Args:
    pdf_url (str): The URL of the PDF to summarize.
    """
    print(f"Downloading PDF from {pdf_url}...")
    pdf_content = download_pdf(pdf_url)
    
    print("Generating summary...")
    summary = summarize_pdf(pdf_content)
    
    print("\nSummary:")
    print(summary)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize a PDF from a given URL using Gemini 1.5 Flash.")
    parser.add_argument("url", help="The URL of the PDF to summarize")
    args = parser.parse_args()

    main(args.url)