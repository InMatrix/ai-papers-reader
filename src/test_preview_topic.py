import json
import os
from datetime import date
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from preview_topic import (
    aggregate_by_topic,
    format_text_report,
    list_paper_metadata_files,
    parse_preview_response,
    preview_weeks,
    resolve_week_selection,
    setup_argparse,
)


def _touch_metadata(directory, date_str, content="Title: Sample\n---\n"):
    path = directory / f"paper_metadata_{date_str}.txt"
    path.write_text(content)
    return path


@pytest.fixture
def metadata_dir(tmp_path):
    for d in ("2024-06-21", "2025-01-10", "2026-01-02", "2026-07-03", "2026-08-02"):
        _touch_metadata(tmp_path, d)
    # Non-matching files should be ignored
    (tmp_path / "status.json").write_text("{}")
    (tmp_path / "notes.txt").write_text("ignore")
    return tmp_path


def test_list_paper_metadata_files_last_n(metadata_dir):
    paths = list_paper_metadata_files(metadata_dir, weeks=2)
    dates = [os.path.basename(p).replace("paper_metadata_", "").replace(".txt", "") for p in paths]
    assert dates == ["2026-07-03", "2026-08-02"]


def test_list_paper_metadata_files_since_until(metadata_dir):
    paths = list_paper_metadata_files(
        metadata_dir,
        since=date(2025, 1, 1),
        until=date(2026, 1, 31),
    )
    dates = [os.path.basename(p).replace("paper_metadata_", "").replace(".txt", "") for p in paths]
    assert dates == ["2025-01-10", "2026-01-02"]


def test_list_paper_metadata_files_since_then_weeks(metadata_dir):
    paths = list_paper_metadata_files(
        metadata_dir,
        since=date(2024, 1, 1),
        weeks=3,
    )
    dates = [os.path.basename(p).replace("paper_metadata_", "").replace(".txt", "") for p in paths]
    assert dates == ["2026-01-02", "2026-07-03", "2026-08-02"]


def test_list_paper_metadata_files_invalid_weeks(metadata_dir):
    with pytest.raises(ValueError, match="--weeks must be >= 1"):
        list_paper_metadata_files(metadata_dir, weeks=0)


def test_resolve_week_selection_defaults_to_four(metadata_dir):
    parser = setup_argparse()
    args = parser.parse_args(["--paper_data_dir", str(metadata_dir)])
    paths = resolve_week_selection(args)
    assert len(paths) == 4
    assert paths[-1].endswith("paper_metadata_2026-08-02.txt")


def test_resolve_week_selection_since_without_default_cap(metadata_dir):
    parser = setup_argparse()
    args = parser.parse_args(
        ["--paper_data_dir", str(metadata_dir), "--since", "2024-01-01"]
    )
    paths = resolve_week_selection(args)
    assert len(paths) == 5


def test_aggregate_and_format_report():
    week_results = [
        {
            "week": "2026-07-03",
            "paper_data_path": "paper_data/paper_metadata_2026-07-03.txt",
            "topics": [
                {
                    "topic": "AI Agents",
                    "papers": [
                        {
                            "title": "Paper A",
                            "url": "https://arxiv.org/pdf/1",
                            "relevance": "Relevant because agents.",
                        }
                    ],
                }
            ],
        },
        {
            "week": "2026-08-02",
            "paper_data_path": "paper_data/paper_metadata_2026-08-02.txt",
            "topics": [
                {
                    "topic": "AI Agents",
                    "papers": [
                        {
                            "title": "Paper B",
                            "url": "https://arxiv.org/pdf/2",
                            "relevance": "Also about agents.",
                        }
                    ],
                }
            ],
        },
    ]

    by_topic = aggregate_by_topic(week_results)
    assert list(by_topic.keys()) == ["AI Agents"]
    assert len(by_topic["AI Agents"]) == 2

    report = format_text_report(week_results)
    assert "## AI Agents" in report
    assert "### Week 2026-07-03" in report
    assert "Paper A" in report
    assert "Paper B" in report


def test_parse_preview_response_rejects_invalid_json_without_writing(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    with pytest.raises(ValueError, match="not valid JSON"):
        parse_preview_response("not json at all")
    assert not Path("error_response.txt").exists()


def test_parse_preview_response_strips_fences():
    payload = [{"topic": "T", "papers": []}]
    wrapped = f"```json\n{json.dumps(payload)}\n```"
    assert parse_preview_response(wrapped) == payload


def test_preview_weeks_no_summarize_or_status(tmp_path):
    week1 = _touch_metadata(tmp_path, "2026-07-03", "Paper data week 1")
    week2 = _touch_metadata(tmp_path, "2026-08-02", "Paper data week 2")
    topics_path = tmp_path / "_topics.yaml"
    topics_path.write_text(
        "- topic: Topic 1\n  description: |\n    Desc 1\n"
    )
    prompt_template = tmp_path / "recommend_papers.txt"
    prompt_template.write_text("topics:\n{topics}\npapers:\n{paper_data}\n")

    mock_response = [
        {
            "topic": "Topic 1",
            "papers": [
                {
                    "title": "Matched Paper",
                    "url": "https://arxiv.org/pdf/123",
                    "relevance": "Fits the topic.",
                }
            ],
        }
    ]

    mock_client = Mock()

    with patch("preview_topic.generate_text") as mock_generate, \
         patch("generate_report.summarize_pdf") as mock_summarize, \
         patch("generate_report.update_status") as mock_update_status, \
         patch("generate_report.generate_report") as mock_generate_report:

        mock_generate.return_value = json.dumps(mock_response)

        results = preview_weeks(
            mock_client,
            [str(week1), str(week2)],
            topics_path=str(topics_path),
            prompt_template_path=str(prompt_template),
            provider="deepseek",
            model="deepseek-v4-flash",
        )

        assert len(results) == 2
        assert results[0]["week"] == "2026-07-03"
        assert results[1]["week"] == "2026-08-02"
        assert results[0]["topics"][0]["papers"][0]["title"] == "Matched Paper"
        assert mock_generate.call_count == 2

        mock_summarize.assert_not_called()
        mock_update_status.assert_not_called()
        mock_generate_report.assert_not_called()
