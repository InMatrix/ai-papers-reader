import os
import yaml

# Format link title as "Report YYYY-MM-DD"
def formatTitle(file_path):
    parts = file_path[5:-3].split('_')
    return ' '.join(word.capitalize() for word in parts)    

markdown_files = []
for root, _, files in os.walk("docs"):
    if "_site" in root:
        continue
    if root == "docs":
        # skip docs/index.md
        continue
    for file in files:
        if file.endswith(".md") and file.startswith("index"):
            file_path = os.path.join(root, file)
            report_date = root[5:]
            markdown_files.append({
                "title": report_date,
                "url": report_date
            })


markdown_files.sort(key=lambda x: x.get("title"), reverse=True)

with open("docs/_data/markdown_files.yml", "w") as outfile:
    yaml.dump(markdown_files, outfile, default_flow_style=False)

print("Markdown files list updated")