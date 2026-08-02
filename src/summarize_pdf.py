"""
PDF summarizer using Gemini or DeepSeek models.

This script downloads a PDF from a given URL and generates a summary. Gemini
receives the uploaded PDF directly; DeepSeek receives text extracted locally
from the PDF.

Provider/model selection is read from the tracked config.yaml file. Credentials
are loaded from the local .env file or the process environment.
"""

import argparse
import os
import requests
import tempfile
import frontmatter
import re
import time
from io import BytesIO
from pypdf import PdfReader, PdfWriter
from llm_client import (
    create_client,
    generate_text,
    load_config,
    resolve_model,
    resolve_provider,
)

# Initialize client lazily
_client = None
_client_provider = None

def get_client(provider=None):
    """
    Get or create the generative AI client.
    """
    global _client, _client_provider
    provider = resolve_provider(provider)
    if _client is None or _client_provider != provider:
        _client = create_client(provider)
        _client_provider = provider
    return _client

def download_pdf(url):
    """
    Download a PDF file from the given URL.

    Args:
    url (str): The URL of the PDF file to download.

    Returns:
    bytes: The content of the PDF file.
    """
    config = load_config()
    timeout = float(config.get("pdf", {}).get("download_timeout_seconds", 120))
    response = requests.get(url, timeout=timeout)
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

def upload_file_with_retry(file_path, display_name, max_retries=5, initial_delay=1, client=None):
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
    from google.genai import types
    
    client = client or get_client("gemini")
    delay = initial_delay
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            uploaded_file = client.files.upload(
                file=file_path,
                config=types.UploadFileConfig(display_name=display_name)
            )
            if attempt > 0:
                print(f"Successfully uploaded file after {attempt + 1} attempt(s)")
            return uploaded_file
        except Exception as e:
            last_exception = e
            error_str = str(e).lower()
            
            # Check if it's a retryable error (503, 429, 500, 502, 504)
            # The new SDK may wrap these differently, so we check the error message
            is_retryable = any(code in error_str for code in ['503', '429', '500', '502', '504', 'unavailable', 'rate limit'])
            
            if is_retryable:
                if attempt < max_retries - 1:
                    print(f"Upload attempt {attempt + 1} failed: {str(e)}. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay *= 2  # Exponential backoff
                else:
                    print(f"Upload failed after {max_retries} attempts")
            else:
                # Non-retryable error, raise immediately
                raise
    
    # If we exhausted all retries, raise the last exception
    raise last_exception

def extract_pdf_text(pdf_content, max_pages=None):
    """Extract a bounded text prefix for providers without PDF upload APIs."""
    config = load_config()
    if max_pages is None:
        max_pages = int(config.get("pdf", {}).get("max_pages", 12))
    if max_pages < 1:
        raise ValueError("DEEPSEEK_MAX_PAGES must be at least 1")

    reader = PdfReader(BytesIO(pdf_content))
    pages = reader.pages[:max_pages]
    if len(reader.pages) > max_pages:
        print(f"Limiting DeepSeek PDF input to the first {max_pages} pages")
    text = "\n\n".join(page.extract_text() or "" for page in pages).strip()
    if not text:
        raise ValueError("No text could be extracted from the PDF")
    return text


def truncate_pdf(pdf_content, max_pages=None, max_bytes=None):
    """Return the original PDF or a first-pages copy when it exceeds the cap."""
    config = load_config()
    pdf_config = config.get("pdf", {})
    if max_bytes is None:
        max_bytes = int(pdf_config.get("max_bytes", 20 * 1024 * 1024))
    if len(pdf_content) <= max_bytes:
        return pdf_content

    if max_pages is None:
        max_pages = int(pdf_config.get("max_pages", 12))
    if max_pages < 1:
        raise ValueError("MAX_PDF_PAGES must be at least 1")

    reader = PdfReader(BytesIO(pdf_content))
    writer = PdfWriter()
    for page in reader.pages[:max_pages]:
        writer.add_page(page)

    output = BytesIO()
    writer.write(output)
    truncated_content = output.getvalue()
    print(
        f"PDF is {len(pdf_content)} bytes; limiting Gemini input to the first "
        f"{min(max_pages, len(reader.pages))} pages ({len(truncated_content)} bytes)"
    )
    return truncated_content


def summarize_pdf(pdf_content, client=None, provider=None, model=None):
    """
    Summarize the content of a PDF using the selected provider and model.

    Args:
    pdf_content (bytes): The content of the PDF file.

    Returns:
    str: A 500-word summary of the PDF content.
    """
    provider = resolve_provider(provider)
    model = resolve_model(provider, model)
    client = client or get_client(provider)

    with open('prompts/summarize_paper.txt', 'r') as file:
        prompt = file.read().strip()

    if provider == "deepseek":
        paper_text = extract_pdf_text(pdf_content)
        response_text = generate_text(
            client,
            f"{prompt}\n\n<paper>\n{paper_text}\n</paper>",
            provider=provider,
            model=model,
        )
        return clean_markdown_blocks(response_text)
    
    # Gemini can process PDFs directly. Keep the complete document below the
    # size cap, and use a first-pages PDF for unusually large documents.
    gemini_pdf_content = truncate_pdf(pdf_content)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
        temp_pdf.write(gemini_pdf_content)
        temp_pdf.flush()
        
        # Upload the PDF file with retry logic
        uploaded_file = upload_file_with_retry(
            temp_pdf.name, "paper.pdf", client=client
        )
        
    try:
        response = client.models.generate_content(
            model=model,
            contents=[prompt, uploaded_file]
        )
    except Exception as e:
        print(f"Error generating content: {e}")
        return None
    finally:
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

def pdf_to_summary(pdf_url, summary_path, client=None, provider=None, model=None):
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
    summary = summarize_pdf(
        pdf_content, client=client, provider=provider, model=model
    )

    if summary is None:
        print(f"Failed to generate summary for {pdf_url}")
        return None

    # Add front matter to the summary
    print(">>> Adding front matter...")
    summary_with_front_matter = add_front_matter(summary, summary_path)

    return summary_with_front_matter

def main(pdf_url, save_location, client=None, provider=None, model=None):
    """
    Main function to orchestrate the PDF download and summarization process.

    Args:
    pdf_url (str): The URL of the PDF to summarize.
    save_location (str): Optional. The directory to save the summary file. Default is "docs/summaries".
    """
    summary_path = get_summary_path(pdf_url, save_location)

    provider = resolve_provider(provider)
    model = resolve_model(provider, model)
    client = client or create_client(provider)
    summary_content = pdf_to_summary(
        pdf_url,
        summary_path,
        client=client,
        provider=provider,
        model=model,
    )

    if summary_content is None:
        print(f"Failed to generate summary for {pdf_url}")
        return None

    print(f">>> Saving summary to {summary_path}\n")
    save_summary(summary_content, summary_path)
    return summary_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Summarize a PDF using Gemini or DeepSeek."
    )
    parser.add_argument("url", help="The URL of the PDF to summarize")
    parser.add_argument("--save_location", default="docs/summaries", help="Directory to save the summary file. Default is 'docs/summaries'.")
    parser.add_argument("--provider", choices=["gemini", "deepseek"], help="LLM provider")
    parser.add_argument("--model", help="Model ID")
    args = parser.parse_args()

    provider = resolve_provider(args.provider)
    model = resolve_model(provider, args.model)
    main(args.url, args.save_location, provider=provider, model=model)
