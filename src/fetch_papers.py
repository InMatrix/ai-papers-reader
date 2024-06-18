import requests

# get papers metadata from endpoint
def get_daily_papers_metadata():
    """
    Retrieves metadata of the Hugging Face daily papers.

    Returns:
        list: A list of dictionaries containing paper metadata.
    """
    base_url = "https://huggingface.co/api/daily_papers"

    all_papers = []
    response = requests.get(base_url)

    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}")

    papers = response.json()
    all_papers.extend(papers)

    return all_papers

# save metadata to variable
papers_metadata = get_daily_papers_metadata()

# save the paper metadata to a file
with open('paper_metadata.txt', 'w') as file:
  for paper in papers_metadata:
    file.write(f"Title: {paper['title']}\n")
    file.write(f"PDF: https://arxiv.org/pdf/{paper['paper']['id']}\n")
    summary = paper['paper']['summary'].replace('\n', '')
    file.write(f"Summary: {summary}\n")
    file.write("---\n")
