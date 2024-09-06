import sys
import requests
from bs4 import BeautifulSoup
import os
import re

def clean_equation(text):
    # Remove italics markers
    text = re.sub(r'italic_(\w)', r'\1', text)
    
    # Convert superscripts
    text = re.sub(r'(\w+)superscript([^\s]+)', r'\1^\2', text)
    
    # Convert subscripts
    text = re.sub(r'(\w+)subscript([^\s]+)', r'\1_\2', text)
    
    # Remove start and end markers for super/subscripts
    text = re.sub(r'start_POSTSUPERSCRIPT|end_POSTSUPERSCRIPT|start_POSTSUBSCRIPT|end_POSTSUBSCRIPT', '', text)
    
    # Convert O(n) notation
    text = re.sub(r'O⁢\((.*?)\)', r'O(\1)', text)
    
    return text

def extract_figures(url):
    # Extract paper ID from the URL
    paper_id = url.split('/')[-1]
    
    # Construct the base URL for images
    base_img_url = f"https://arxiv.org/html/{paper_id}/"

    # Fetch the HTML content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all figure elements
    figures = soup.find_all('figure')

    # Create a directory to store the figures
    dir_name = f"figures_{paper_id}"
    os.makedirs(dir_name, exist_ok=True)

    # Extract and save each figure
    for i, figure in enumerate(figures, 1):
        # Extract image source
        img = figure.find('img')
        if img and 'src' in img.attrs:
            img_src = img['src']
            img_url = base_img_url + img_src

            # Download and save the image
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                img_filename = os.path.join(dir_name, f"figure_{i}.png")
                with open(img_filename, 'wb') as f:
                    f.write(img_response.content)
                print(f"Saved figure {i} as {img_filename}")
            else:
                print(f"Failed to download image {i} from {img_url}")

        # Extract caption
        caption = figure.find('figcaption')
        if caption:
            caption_text = re.sub(r'\s+', ' ', caption.get_text().strip())
            caption_text = clean_equation(caption_text)
            caption_filename = os.path.join(dir_name, f"figure_{i}_caption.txt")
            with open(caption_filename, 'w', encoding='utf-8') as f:
                f.write(caption_text)
            print(f"Saved caption for figure {i} as {caption_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <arxiv_html_url>")
        sys.exit(1)

    url = sys.argv[1]
    extract_figures(url)