#!/bin/bash

# Regenerate reports for all the paper metadata files in the paper_data directory
# Run this script from the root directory of the project
# Example usage: bash src/regenerate_reports.sh

# Loop through each file in the paper_data directory
for file in ./paper_data/*; do
  # Extract the filename without the path
  filename=$(basename -- "$file")
  
  # Replace 'paper_metadata' with 'report' in the filename for the report path
  report_filename="${filename/paper_metadata/report}"
  
  # Construct the report path with the modified filename
  report_path="docs/${report_filename%.txt}.md"
  
  # Run the generate_report.py script with the current file and report path
  python src/generate_report.py --paper_data_path "paper_data/$filename" --report_path "$report_path"
done