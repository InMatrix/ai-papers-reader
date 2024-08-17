#!/bin/bash

# Run the full pipeline of generating a papers report

python src/fetch_papers.py
python src/generate_report.py
python src/list_md_files.py