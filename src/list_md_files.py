import os
import yaml
import frontmatter

# Format link title as "Report YYYY-MM-DD"
def formatTitle(file_path):
    parts = file_path[8:-3].split('_')
    return ' '.join(word.capitalize() for word in parts)    

markdown_files = []
for root, _, files in os.walk("docs"):
    for file in files:
        if file.endswith(".md") and not(file.startswith("index")):
            file_path = os.path.join(root, file)
            # post = frontmatter.load(file_path)
            markdown_files.append({
                "title": formatTitle(file_path),
                "url": file_path[8:-3],  
            })

markdown_files.sort(key=lambda x: x.get("title"), reverse=True)

with open("docs/_data/markdown_files.yml", "w") as outfile:
    yaml.dump(markdown_files, outfile, default_flow_style=False)
