import os
import datetime
import google.generativeai as genai

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
model = genai.GenerativeModel('gemini-1.5-flash')

with open('paper_data/paper_metadata.txt', 'r') as file:
    paper_data = file.read()

prompt = f'''
You’re my research assistant with PhD-level knowledge in both Machine Learning (ML) and Human-Computer Interaction (HCI). I hired you to help me keep track of latest papers at the intersection of Generative AI and HCI.

The text delimited by triple quotes include a list of recently published AI papers. Each entry include three fields: "title", "PDF", and "summary". The PDF field include a link to download the PDF file of the paper from [arxiv.org](http://arxiv.org/). You job is to analyze this text and identify papers relevant to the following research questions:

- How are users involved in the evaluation of AI systems?
- What are the novel prompt engineering techniques that improve the performance of AI systems?
- How can the human-in-the-loop approach improve the model training process?
- What are the latest applications of generative AI in user interface design and engineering?
- How to make it easier to explain AI system’s behavior?

Your response should include a number of entries formatted as follows. The text in curly braces are placeholders.

**{{Research Question}}**

- *Relevant Paper*: {{paper title}}
    - *Why it's relevant*: {{briefly summarize the aspects of the paper relevant to the research question}}
    - *Read more*: {{link to the paper's PDF file}}

If there are multiple relevant papers for a given research question, list all of them. If none is relevant, print "no relevant paper was found for this question."

"""
{paper_data}
"""
'''

response = model.generate_content(prompt)
# print(response.text)

# Write response to a file
date_suffix = datetime.date.today().strftime('%Y-%m-%d')

with open(f'reports/report_{date_suffix}.md', 'w') as file:
    file.write(response.text)