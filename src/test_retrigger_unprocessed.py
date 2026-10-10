import json
import subprocess
from unittest.mock import patch

import pytest

import retrigger_unprocessed


@pytest.fixture
def incomplete_weeks(tmp_path, monkeypatch):
    """Two metadata files with no report yet, in a temporary working tree."""
    paper_data = tmp_path / "paper_data"
    paper_data.mkdir()
    status = {}
    for date in ("2026-01-02", "2026-01-09"):
        filename = f"paper_metadata_{date}.txt"
        (paper_data / filename).write_text("Title: Paper\n")
        status[filename] = {"final_report_generated": False}
    (paper_data / "status.json").write_text(json.dumps(status))

    monkeypatch.setattr(retrigger_unprocessed, "PAPER_DATA_DIR", str(paper_data))
    monkeypatch.setattr(
        retrigger_unprocessed, "STATUS_FILE", str(paper_data / "status.json")
    )
    monkeypatch.setattr(retrigger_unprocessed, "DOCS_DIR", str(tmp_path / "docs"))


def run_failing_for(*failing_fragments):
    """A subprocess.run stand-in that fails commands mentioning a fragment."""

    def run(command, check):
        if any(fragment in " ".join(command) for fragment in failing_fragments):
            raise subprocess.CalledProcessError(1, command)
        return subprocess.CompletedProcess(command, 0)

    return run


def test_main_exits_zero_when_every_report_generates(incomplete_weeks):
    with patch("retrigger_unprocessed.subprocess.run", side_effect=run_failing_for()) as run:
        retrigger_unprocessed.main()

    assert run.call_count == 3  # two reports and the index


def test_main_exits_nonzero_after_processing_the_remaining_files(incomplete_weeks):
    with patch(
        "retrigger_unprocessed.subprocess.run",
        side_effect=run_failing_for("paper_metadata_2026-01-02.txt"),
    ) as run:
        with pytest.raises(SystemExit) as exit_info:
            retrigger_unprocessed.main()

    assert "paper_metadata_2026-01-02.txt" in str(exit_info.value)
    assert "paper_metadata_2026-01-09.txt" not in str(exit_info.value)
    # The later week and the index update still ran
    commands = [" ".join(call.args[0]) for call in run.call_args_list]
    assert any("paper_metadata_2026-01-09.txt" in command for command in commands)
    assert any("list_md_files.py" in command for command in commands)


def test_main_exits_nonzero_when_the_index_update_fails(incomplete_weeks):
    with patch(
        "retrigger_unprocessed.subprocess.run",
        side_effect=run_failing_for("list_md_files.py"),
    ):
        with pytest.raises(SystemExit) as exit_info:
            retrigger_unprocessed.main()

    assert "the report index" in str(exit_info.value)
