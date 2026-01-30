import os
import json
import glob
import subprocess
import time

STATUS_FILE = "paper_data/status.json"
PAPER_DATA_DIR = "paper_data"
DOCS_DIR = "docs"

def extract_date_from_paper_data_path(paper_data_path):
    # e.g., paper_metadata_2024-06-21.txt -> 2024-06-21
    return paper_data_path.split("_")[-1].split(".")[0]

def backfill_status():
    """
    Scans for existing reports and marks corresponding data files as completed in status.json
    if they are not already tracked.
    """
    print("Backfilling status.json based on existing reports...")

    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r") as f:
            try:
                status_data = json.load(f)
            except json.JSONDecodeError:
                status_data = {}
    else:
        status_data = {}

    paper_files = glob.glob(os.path.join(PAPER_DATA_DIR, "paper_metadata_*.txt"))

    updates_made = False

    for paper_path in paper_files:
        filename = os.path.basename(paper_path)
        date_string = extract_date_from_paper_data_path(filename)
        report_path = os.path.join(DOCS_DIR, date_string, "index.md")

        # If the report exists, consider it done for legacy files
        if os.path.exists(report_path):
            if filename not in status_data:
                print(f"Marking {filename} as completed (legacy backfill).")
                status_data[filename] = {
                    "initial_report_generated": True,
                    "papers_summarized": {}, # We don't know the details, but that's fine for legacy
                    "final_report_generated": True,
                    "last_updated": time.strftime("%Y-%m-%dT%H:%M:%S")
                }
                updates_made = True
            elif not status_data[filename].get("final_report_generated"):
                # If it exists in status but marked incomplete, but the file exists on disk...
                # We might want to trust the status file more?
                # Or assume if index.md is there, it's "good enough"?
                # For now, let's respect status.json if it exists, assuming it's more accurate about *completion*
                # (e.g. maybe it crashed halfway through summaries).
                pass

    if updates_made:
        with open(STATUS_FILE, "w") as f:
            json.dump(status_data, f, indent=2)
        print("Status backfill complete.")
    else:
        print("No backfill needed.")


def process_incomplete():
    """
    Finds unprocessed or incomplete data files and runs generate_report.py for them.
    """
    print("Checking for incomplete items...")

    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r") as f:
            try:
                status_data = json.load(f)
            except json.JSONDecodeError:
                status_data = {}
    else:
        status_data = {}

    paper_files = glob.glob(os.path.join(PAPER_DATA_DIR, "paper_metadata_*.txt"))
    # Sort to process oldest first (or newest? usually oldest to catch up)
    paper_files.sort()

    for paper_path in paper_files:
        filename = os.path.basename(paper_path)

        needs_processing = False

        if filename not in status_data:
            print(f"Found new/untracked file: {filename}")
            needs_processing = True
        elif not status_data[filename].get("final_report_generated"):
            print(f"Found incomplete file: {filename}")
            needs_processing = True

        if needs_processing:
            print(f"Triggering report generation for {filename}...")
            date_string = extract_date_from_paper_data_path(filename)
            report_path = os.path.join(DOCS_DIR, date_string, "index.md")
            try:
                # Call generate_report.py
                subprocess.run(
                    ["python", "src/generate_report.py", "--paper_data_path", paper_path, "--report_path", report_path],
                    check=True
                )
                print(f"Successfully processed {filename}")
            except subprocess.CalledProcessError as e:
                print(f"Error processing {filename}: {e}")
                # Continue to next file instead of crashing the whole pipeline
                continue


def main():
    # 1. Backfill legacy items first
    backfill_status()

    # 2. Process anything that is still pending
    process_incomplete()

    # 3. Update the index
    print("Updating report index...")
    try:
        subprocess.run(["python", "src/list_md_files.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error updating index: {e}")

if __name__ == "__main__":
    main()
