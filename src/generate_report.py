import os
import datetime
import google.generativeai as genai
import frontmatter

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
model = genai.GenerativeModel('gemini-1.5-flash')

paper_data = read_file('paper_data/paper_metadata.txt')

prompt_template = read_file('prompts/identify_papers.txt')

prompt = prompt_template.replace("{paper_data}", paper_data)

response = model.generate_content(prompt)
# print(response.text)

# Add the current date to the top of the file
date = datetime.datetime.now().strftime("%Y-%m-%d")

modified_text = f"## {date}\n\n" + response.text

# Create a post with frontmatter
post = frontmatter.loads(modified_text)
post.metadata['layout'] = 'post'

# Convert back to string with frontmatter
modified_text = frontmatter.dumps(post)

# set layout of the output to 'post'

# Write the modified text to a file
with open(f'docs/report_latest.md', 'w') as file:
    file.write(modified_text)