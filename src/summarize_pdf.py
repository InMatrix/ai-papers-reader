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
- frontmatter library

Usage:
1. Install required libraries:
   pip install google-generativeai requests frontmatter

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
import frontmatter
import re
import time

# Configure the generative AI model
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-2.5-flash-lite-preview-06-17')

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

def get_summary_path(pdf_url, save_location):
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

def clean_markdown_blocks(text):
    """
    Remove markdown code block markers from the text.

    Args:
    text (str): The text to clean.

    Returns:
    str: The text with markdown code block markers removed.
    """
    # Remove ```markdown at the start and ``` at the end if they exist
    text = re.sub(r'^```markdown\s*\n', '', text)
    text = re.sub(r'\n```\s*$', '', text)
    return text

def upload_file_with_retry(file_path, display_name, max_retries=5, initial_delay=1):
    """
    Upload a file to Gemini with retry logic for handling transient errors.
    
    Args:
    file_path (str): Path to the file to upload.
    display_name (str): Display name for the uploaded file.
    max_retries (int): Maximum number of retry attempts. Default is 5.
    initial_delay (int): Initial delay in seconds before first retry. Default is 1.
    
    Returns:
    The uploaded file object.
    
    Raises:
    Exception: If all retry attempts fail.
    """
    from googleapiclient.errors import ResumableUploadError, HttpError
    
    delay = initial_delay
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            uploaded_file = genai.upload_file(path=file_path, display_name=display_name)
            if attempt > 0:
                print(f"Successfully uploaded file after {attempt + 1} attempt(s)")
            return uploaded_file
        except (ResumableUploadError, HttpError) as e:
            last_exception = e
            # Check if it's a 503 Service Unavailable or other transient error
            if hasattr(e, 'resp') and hasattr(e.resp, 'status'):
                status_code = e.resp.status
            else:
                # Try to extract status from error message
                status_code = 503 if '503' in str(e) else None
            
            # Retry on 503, 429 (rate limit), 500, 502, 504 errors
            if status_code in [500, 502, 503, 504, 429]:
                if attempt < max_retries - 1:
                    print(f"Upload attempt {attempt + 1} failed with status {status_code}: {str(e)}. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay *= 2  # Exponential backoff
                else:
                    print(f"Upload failed after {max_retries} attempts")
            else:
                # Non-retryable error, raise immediately
                raise
        except Exception as e:
            # For other unexpected exceptions, raise immediately
            print(f"Unexpected error during upload: {e}")
            raise
    
    # If we exhausted all retries, raise the last exception
    raise last_exception

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
        
        # Upload the PDF file with retry logic
        uploaded_file = upload_file_with_retry(path=temp_pdf.name, display_name="paper.pdf")
        
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
    
    # Clean the response text of markdown code block markers
    return clean_markdown_blocks(response.text)

def add_front_matter(summary, summary_path):
    """
    Adds front matter to the summary using the frontmatter package.

    Args:
    summary (str): The summary to which front matter will be added.
    summary_path (str): The path of the summary file, used to generate the permalink.

    Returns:
    str: The summary with added front matter.
    """
    # Extract the title from the first line of the summary
    title_line = summary.split('\n', 1)[0]

    summary = summary.replace(title_line, '')
    # Remove all the leading or trailing '#', '*' and whitespace
    title = title_line.strip('#* ')
    
    # Replace colons in the title with the HTML entity &#58;
    title = title.replace(':', '&#58;')
    
    # Generate the permalink based on the summary file's path
    permalink = summary_path.replace(".md", "/").replace("docs/","")

    # Extract the PDF URL from the permalink
    # PDF URL pattern: https://arxiv.org/pdf/2409.02392
    pdf_url = f"https://arxiv.org/pdf/{permalink.split('/')[-2]}"
    
    # Create a front matter dictionary
    front_matter_dict = {
        'layout': 'paper',
        'title': title,
        'pdf_url': pdf_url,
        'permalink': permalink
    }

    # Create a frontmatter post object
    post = frontmatter.Post(summary)
    post.metadata = front_matter_dict
    
    # Convert the post object to a string with front matter
    return frontmatter.dumps(post)

def save_summary(summary, output_file):
    """
    Save the summary to a file.

    Args:
    summary (str): The summary to save.
    output_file (str): The path to the output file.
    """
    with open(output_file, 'w') as f:
        f.write(summary)

def pdf_to_summary(pdf_url, summary_path):
    """
    Get the content of the summary for a given PDF URL without saving it to a file.
    Args:
    pdf_url (str): The URL of the PDF file.

    Returns:
    str: The content of the summary.
    """
    if os.path.exists(summary_path):
        print(f"Summary for {pdf_url} already exists at {summary_path}")
        # Return the content of the existing summary file
        with open(summary_path, 'r') as f:
            return f.read()
    
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

    return summary_with_front_matter

def main(pdf_url, save_location):
    """
    Main function to orchestrate the PDF download and summarization process.

    Args:
    pdf_url (str): The URL of the PDF to summarize.
    save_location (str): Optional. The directory to save the summary file. Default is "docs/summaries".
    """
    summary_path = get_summary_path(pdf_url, save_location)

    summary_content = pdf_to_summary(pdf_url, summary_path)

    if summary_content is None:
        print(f"Failed to generate summary for {pdf_url}")
        return None

    print(f">>> Saving summary to {summary_path}\n")
    save_summary(summary_content, summary_path)
    return summary_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize a PDF from a given URL using Gemini 1.5 Flash.")
    parser.add_argument("url", help="The URL of the PDF to summarize")
    parser.add_argument("--save_location", default="docs/summaries", help="Directory to save the summary file. Default is 'docs/summaries'.")
    args = parser.parse_args()

    main(args.url, args.save_location)