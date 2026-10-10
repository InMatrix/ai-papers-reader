import os
import subprocess
from pathlib import Path

import pytest

PIPELINE_SCRIPT = Path(__file__).resolve().parent / "fetch_generate_publish.sh"


def run_pipeline(tmp_path, failing_script=None):
    """Run the pipeline script with a stand-in `python` that records each call."""
    calls = tmp_path / "calls.txt"
    fake_python = tmp_path / "python"
    fake_python.write_text(
        "#!/bin/bash\n"
        f'echo "$1" >> "{calls}"\n'
        f'[ "$1" != "src/{failing_script}" ]\n'
    )
    fake_python.chmod(0o755)

    result = subprocess.run(
        ["bash", str(PIPELINE_SCRIPT)],
        env={**os.environ, "PATH": f"{tmp_path}{os.pathsep}{os.environ['PATH']}"},
    )
    return result.returncode, calls.read_text().split()


def test_pipeline_succeeds_when_every_step_succeeds(tmp_path):
    returncode, calls = run_pipeline(tmp_path)

    assert returncode == 0
    assert calls == [
        "src/fetch_papers.py",
        "src/generate_report.py",
        "src/list_md_files.py",
    ]


@pytest.mark.parametrize("failing_script", ["generate_report.py", "list_md_files.py"])
def test_pipeline_fails_after_running_every_step(tmp_path, failing_script):
    returncode, calls = run_pipeline(tmp_path, failing_script)

    assert returncode == 1
    assert calls == [
        "src/fetch_papers.py",
        "src/generate_report.py",
        "src/list_md_files.py",
    ]


def test_pipeline_skips_report_generation_when_the_fetch_fails(tmp_path):
    returncode, calls = run_pipeline(tmp_path, "fetch_papers.py")

    assert returncode == 1
    assert calls == ["src/fetch_papers.py", "src/list_md_files.py"]
