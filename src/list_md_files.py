import os
import yaml
import frontmatter

markdown_files = []
for root, _, files in os.walk("reports"):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            post = frontmatter.load(file_path)
            markdown_files.append({
                "title": post.get("title", file),
                "url": file_path[8:-3],  
                # Remove the leading "reports/" and the trailing ".md"
                "date": post.get("date", "N/A")
            })

with open("_data/markdown_files.yml", "w") as outfile:
    yaml.dump(markdown_files, outfile, default_flow_style=False)
