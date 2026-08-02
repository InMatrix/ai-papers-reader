# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI Papers Reader is an AI agent that automatically generates weekly digests of AI papers from Hugging Face Daily Papers. It uses Google Gemini or DeepSeek to filter and summarize papers based on customizable topics, publishing results to a static website via Netlify.

## Commands

### Setup
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export GOOGLE_API_KEY=your_key_here
# Or: export LLM_PROVIDER=deepseek DEEPSEEK_API_KEY=your_key_here
```

### Run Full Pipeline
```bash
bash src/fetch_generate_publish.sh
```

### Run Tests
```bash
python src/test_generate_report.py
python src/test_summarize_pdf.py
```

## Architecture

The pipeline flows: **Hugging Face API → Fetch → Filter/Summarize with LLM → Generate Markdown → Publish**

Key components in `src/`:
- `fetch_papers.py` - Fetches paper metadata from Hugging Face Daily Papers API
- `generate_report.py` - Uses Gemini LLM to filter papers and generate summaries
- `summarize_pdf.py` - PDF summarization with figure extraction
- `json_to_markdown.py` - Converts JSON reports to markdown for web publishing
- `fetch_generate_publish.sh` - Orchestrates the entire pipeline

Data flow:
- `paper_data/` - Raw paper metadata (JSON) and processing status
- `docs/` - Generated markdown reports (published to Netlify)
- `prompts/recommend_papers.txt` - Prompt template controlling paper selection and summarization

## Configuration

- **Topics/Filtering**: Edit `prompts/recommend_papers.txt` to customize which papers are selected
- **LLM**: `LLM_PROVIDER` selects `gemini` (default) or `deepseek`; `LLM_MODEL` overrides the provider's default model
- **API Key**: Requires `GOOGLE_API_KEY` for Gemini or `DEEPSEEK_API_KEY` for DeepSeek
- **Python Version**: 3.12

## CI/CD

GitHub Actions workflows in `.github/workflows/`:
- `fetch_generate_publish.yml` - Weekly automation (Fridays at midnight UTC)
- `retrigger_reports.yml` - Manual trigger to retry failed paper processing

Both workflows use the provider selected by the `LLM_PROVIDER` repository variable and auto-commit generated reports.
