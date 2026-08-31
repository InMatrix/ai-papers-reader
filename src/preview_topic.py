"""
Dry-run preview: replay the first-stage topic matcher over historical paper_data/.

Does NOT download PDFs, summarize, write docs/, or update status.json.

Topic file workflows (--topics):
  - Isolation: a YAML with only the new topic (same schema as prompts/_topics.yaml).
  - Competition: a local copy of _topics.yaml with the new topic appended.
  - When wording looks right, copy into prompts/_topics.yaml for weekly runs.
    Do not edit _topics.yaml just to preview.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

from generate_report import extract_date_from_paper_data_path, inflate_prompt
from llm_client import (
    create_client,
    generate_text,
    load_config,
    resolve_model,
    resolve_provider,
)

PAPER_METADATA_RE = re.compile(r"^paper_metadata_(\d{4}-\d{2}-\d{2})\.txt$")
DEFAULT_WEEKS = 4
DEFAULT_TOPICS = "prompts/_topics.yaml"
DEFAULT_PROMPT_TEMPLATE = "prompts/recommend_papers.txt"


def _log(message):
    """Progress and status messages go to stderr so stdout stays pipeable."""
    print(message, file=sys.stderr)


def _parse_date(value: str) -> date:
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"Invalid date '{value}'. Use YYYY-MM-DD."
        ) from exc


def list_paper_metadata_files(
    paper_data_dir,
    since=None,
    until=None,
    weeks=None,
):
    """
    Return paper_metadata_*.txt paths sorted by date ascending.

    If weeks is set, keep only the most recent N files after applying since/until.
    """
    directory = Path(paper_data_dir)
    if not directory.is_dir():
        raise FileNotFoundError(f"Paper data directory not found: {directory}")

    since_date = _coerce_date(since)
    until_date = _coerce_date(until)

    matched = []
    for path in directory.iterdir():
        if not path.is_file():
            continue
        match = PAPER_METADATA_RE.match(path.name)
        if not match:
            continue
        file_date = datetime.strptime(match.group(1), "%Y-%m-%d").date()
        if since_date is not None and file_date < since_date:
            continue
        if until_date is not None and file_date > until_date:
            continue
        matched.append((file_date, str(path)))

    matched.sort(key=lambda item: item[0])
    paths = [path for _, path in matched]

    if weeks is not None:
        if weeks < 1:
            raise ValueError("--weeks must be >= 1")
        paths = paths[-weeks:]

    return paths


def _coerce_date(value):
    if value is None:
        return None
    if isinstance(value, date):
        return value
    return _parse_date(str(value))


def parse_preview_response(response):
    """
    Parse the model JSON response without writing debug files.

    Unlike generate_report.parse_model_response, this keeps the dry-run
    guarantee (no error_response.txt or other side-effect writes).
    """
    response_text = response.text if hasattr(response, "text") else response
    cleaned_response = response_text.strip()

    if cleaned_response.startswith("```json"):
        cleaned_response = cleaned_response[7:]
    elif cleaned_response.startswith("```"):
        cleaned_response = cleaned_response[3:]

    if cleaned_response.endswith("```"):
        cleaned_response = cleaned_response[:-3]

    start_idx = -1
    for i, char in enumerate(cleaned_response):
        if char in ["{", "["]:
            start_idx = i
            break

    if start_idx > 0:
        cleaned_response = cleaned_response[start_idx:]

    cleaned_response = cleaned_response.strip()

    try:
        return json.loads(cleaned_response)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Model response is not valid JSON for week preview: {exc}"
        ) from exc


def preview_weeks(
    client,
    paper_data_paths,
    topics_path,
    prompt_template_path=DEFAULT_PROMPT_TEMPLATE,
    provider="gemini",
    model=None,
):
    """
    Run first-stage matching for each week. Returns a list of week results:

    [
      {
        "week": "YYYY-MM-DD",
        "paper_data_path": "...",
        "topics": [{"topic": "...", "papers": [...]}]
      },
      ...
    ]
    """
    provider = resolve_provider(provider)
    model = resolve_model(provider, model)
    results = []

    for paper_data_path in paper_data_paths:
        week = extract_date_from_paper_data_path(paper_data_path)
        _log(f"Matching week {week} ({paper_data_path})...")
        prompt, _topics = inflate_prompt(
            prompt_template_path, paper_data_path, topics_path=topics_path
        )
        response_text = generate_text(
            client,
            prompt,
            provider=provider,
            model=model,
            json_output=True,
            temperature=0.7,
        )
        response_json = parse_preview_response(response_text)
        results.append(
            {
                "week": week,
                "paper_data_path": paper_data_path,
                "topics": response_json,
            }
        )

    return results


def aggregate_by_topic(week_results):
    """Group matches as topic -> list of {week, title, url, relevance}."""
    by_topic = defaultdict(list)
    for week_result in week_results:
        week = week_result["week"]
        for topic_block in week_result["topics"]:
            topic_name = topic_block.get("topic", "Unknown")
            for paper in topic_block.get("papers") or []:
                by_topic[topic_name].append(
                    {
                        "week": week,
                        "title": paper.get("title"),
                        "url": paper.get("url"),
                        "relevance": paper.get("relevance"),
                    }
                )
    return dict(by_topic)


def format_text_report(week_results):
    by_topic = aggregate_by_topic(week_results)
    if not by_topic:
        return "No matching papers returned for the selected weeks.\n"

    lines = []
    for topic_name, papers in by_topic.items():
        lines.append(f"## {topic_name}")
        lines.append(f"({len(papers)} match(es) across selected weeks)")
        lines.append("")
        # Group by week within topic
        by_week = defaultdict(list)
        for paper in papers:
            by_week[paper["week"]].append(paper)
        for week in sorted(by_week):
            lines.append(f"### Week {week}")
            for paper in by_week[week]:
                title = paper.get("title") or "(no title)"
                url = paper.get("url") or ""
                relevance = paper.get("relevance") or ""
                lines.append(f"- {title}")
                if url:
                    lines.append(f"  {url}")
                if relevance:
                    lines.append(f"  Relevance: {relevance}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def setup_argparse():
    parser = argparse.ArgumentParser(
        description=(
            "Preview which historical papers a topics YAML would match "
            "(first-stage LLM picker only; no PDF summarization)."
        )
    )
    parser.add_argument(
        "--topics",
        default=DEFAULT_TOPICS,
        help=f"Topics YAML path (default: {DEFAULT_TOPICS})",
    )
    parser.add_argument(
        "--weeks",
        type=int,
        default=None,
        help=(
            f"Use the most recent N weeks after date filters "
            f"(default: {DEFAULT_WEEKS} when --since/--until omitted)"
        ),
    )
    parser.add_argument(
        "--since",
        type=_parse_date,
        help="Include weeks on or after this date (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--until",
        type=_parse_date,
        help="Include weeks on or before this date (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--paper_data_dir",
        default="paper_data",
        help="Directory containing paper_metadata_*.txt (default: paper_data)",
    )
    parser.add_argument(
        "--prompt_template",
        default=DEFAULT_PROMPT_TEMPLATE,
        help=f"Prompt template path (default: {DEFAULT_PROMPT_TEMPLATE})",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of a text report",
    )
    parser.add_argument(
        "--output",
        help="Write report to this path instead of stdout",
    )
    parser.add_argument(
        "--provider",
        choices=["gemini", "deepseek"],
        help="One-off provider override (default: config.yaml)",
    )
    parser.add_argument(
        "--model",
        help="One-off model override (default: config.yaml)",
    )
    return parser


def resolve_week_selection(args):
    """Apply default --weeks=4 when neither since nor until is set."""
    weeks = args.weeks
    if weeks is None and args.since is None and args.until is None:
        weeks = DEFAULT_WEEKS
    return list_paper_metadata_files(
        args.paper_data_dir,
        since=args.since,
        until=args.until,
        weeks=weeks,
    )


def main(argv=None):
    parser = setup_argparse()
    args = parser.parse_args(argv)

    if not os.path.isfile(args.topics):
        raise SystemExit(f"Topics file not found: {args.topics}")
    if not os.path.isfile(args.prompt_template):
        raise SystemExit(f"Prompt template not found: {args.prompt_template}")

    paper_paths = resolve_week_selection(args)
    if not paper_paths:
        raise SystemExit(
            "No paper_metadata_*.txt files matched the selected week filters."
        )

    _log(
        f"Previewing {len(paper_paths)} week(s) with topics from {args.topics} "
        "(first-stage match only; summarization skipped)."
    )

    config = load_config()
    provider = resolve_provider(args.provider, config=config)
    model = resolve_model(provider, args.model, config=config)
    client = create_client(provider)

    week_results = preview_weeks(
        client,
        paper_paths,
        topics_path=args.topics,
        prompt_template_path=args.prompt_template,
        provider=provider,
        model=model,
    )

    payload = {
        "topics_path": args.topics,
        "weeks": [r["week"] for r in week_results],
        "by_topic": aggregate_by_topic(week_results),
        "week_results": week_results,
    }

    if args.json:
        report = json.dumps(payload, indent=2) + "\n"
    else:
        report = format_text_report(week_results)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report)
        _log(f"Wrote preview to {args.output}")
    else:
        # stdout is reserved for the report so --json stays machine-readable
        print(report, end="")


if __name__ == "__main__":
    main()
