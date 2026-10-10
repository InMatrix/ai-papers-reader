#!/bin/bash

# Run the full pipeline of generating a papers report

status=0

# Without freshly fetched metadata, generate_report.py would rerun on an older
# week's file, so skip it when the fetch fails.
python src/fetch_papers.py && python src/generate_report.py || status=1

# Index whatever was published, then report any failure through the exit code
# so the workflow run is marked as failed.
python src/list_md_files.py || status=1

exit $status
