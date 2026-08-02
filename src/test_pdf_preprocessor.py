from types import SimpleNamespace
from unittest.mock import Mock, patch

import pytest
import requests

import pdf_preprocessor


class FakeResponse:
    def __init__(self, chunks=(), status_code=200):
        self.chunks = chunks
        self.status_code = status_code
        self.closed = False

    def raise_for_status(self):
        if self.status_code >= 400:
            error = requests.HTTPError(f"HTTP {self.status_code}")
            error.response = self
            raise error

    def iter_content(self, chunk_size):
        self.chunk_size = chunk_size
        return iter(self.chunks)

    def close(self):
        self.closed = True


class FakeSession:
    def __init__(self, responses):
        self.responses = iter(responses)
        self.calls = []
        self.closed = False

    def get(self, url, **kwargs):
        self.calls.append((url, kwargs))
        response = next(self.responses)
        if isinstance(response, Exception):
            raise response
        return response

    def close(self):
        self.closed = True


def download_config(**overrides):
    config = {
        "pdf": {
            "download_connect_timeout_seconds": 7,
            "download_read_timeout_seconds": 11,
            "download_retries": 2,
            "download_retry_backoff_seconds": 3,
            "download_chunk_size_bytes": 8,
        }
    }
    config["pdf"].update(overrides)
    return config


def test_download_pdf_streams_content_with_split_timeouts(monkeypatch):
    response = FakeResponse([b"%PDF-", b"content"])
    session = FakeSession([response])
    monkeypatch.setattr(
        pdf_preprocessor, "load_config", lambda: download_config()
    )

    assert pdf_preprocessor.download_pdf("https://example.test/paper.pdf", session) == (
        b"%PDF-content"
    )
    url, kwargs = session.calls[0]
    assert url == "https://example.test/paper.pdf"
    assert kwargs["stream"] is True
    assert kwargs["timeout"] == (7.0, 11.0)
    assert kwargs["headers"] == {"Accept": "application/pdf"}
    assert response.closed


def test_download_pdf_retries_transient_timeout(monkeypatch):
    response = FakeResponse([b"complete"])
    session = FakeSession([requests.Timeout("read timed out"), response])
    monkeypatch.setattr(
        pdf_preprocessor,
        "load_config",
        lambda: download_config(download_retries=1, download_retry_backoff_seconds=2),
    )
    with patch.object(pdf_preprocessor.time, "sleep") as sleep:
        assert pdf_preprocessor.download_pdf("https://example.test/paper.pdf", session) == (
            b"complete"
        )

    assert len(session.calls) == 2
    sleep.assert_called_once_with(2)


def test_download_pdf_resumes_after_partial_read_timeout(monkeypatch):
    class FailingResponse(FakeResponse):
        def iter_content(self, chunk_size):
            yield b"partial"
            raise requests.Timeout("read timed out")

    session = FakeSession([FailingResponse(), FakeResponse([b"remainder"], status_code=206)])
    monkeypatch.setattr(
        pdf_preprocessor,
        "load_config",
        lambda: download_config(download_retries=1),
    )
    with patch.object(pdf_preprocessor.time, "sleep"):
        assert pdf_preprocessor.download_pdf("https://example.test/paper.pdf", session) == (
            b"partialremainder"
        )

    assert session.calls[1][1]["headers"]["Range"] == "bytes=7-"


def test_download_pdf_retries_transient_http_status(monkeypatch):
    response = FakeResponse([b"complete"])
    session = FakeSession([FakeResponse(status_code=503), response])
    monkeypatch.setattr(
        pdf_preprocessor,
        "load_config",
        lambda: download_config(download_retries=1),
    )
    with patch.object(pdf_preprocessor.time, "sleep"):
        assert pdf_preprocessor.download_pdf("https://example.test/paper.pdf", session) == (
            b"complete"
        )

    assert len(session.calls) == 2


def test_download_pdf_does_not_retry_non_transient_http_status(monkeypatch):
    session = FakeSession([FakeResponse(status_code=404)])
    monkeypatch.setattr(
        pdf_preprocessor, "load_config", lambda: download_config(download_retries=3)
    )

    with pytest.raises(requests.HTTPError):
        pdf_preprocessor.download_pdf("https://example.test/paper.pdf", session)

    assert len(session.calls) == 1


def test_layout_page_text_reads_left_column_before_right_column():
    words = []
    for index, text in enumerate(("L1", "L2", "L3")):
        words.append(
            {
                "text": text,
                "x0": 50,
                "x1": 62,
                "top": 100 + index * 16,
                "bottom": 110 + index * 16,
                "size": 10,
            }
        )
    for index, text in enumerate(("R1", "R2", "R3")):
        words.append(
            {
                "text": text,
                "x0": 520,
                "x1": 532,
                "top": 100 + index * 16,
                "bottom": 110 + index * 16,
                "size": 10,
            }
        )

    page = SimpleNamespace(width=600, extract_words=lambda **kwargs: words)

    assert pdf_preprocessor._layout_page_text(page, {}) == "L1\nL2\nL3\nR1\nR2\nR3"


def test_layout_page_text_keeps_full_width_heading_before_columns():
    words = [
        {"text": "Paper title", "x0": 50, "x1": 550, "top": 20, "bottom": 32, "size": 16},
    ]
    for index, text in enumerate(("L1", "L2", "L3")):
        words.append(
            {
                "text": text,
                "x0": 50,
                "x1": 62,
                "top": 100 + index * 16,
                "bottom": 110 + index * 16,
                "size": 10,
            }
        )
    for index, text in enumerate(("R1", "R2", "R3")):
        words.append(
            {
                "text": text,
                "x0": 520,
                "x1": 532,
                "top": 100 + index * 16,
                "bottom": 110 + index * 16,
                "size": 10,
            }
        )

    page = SimpleNamespace(width=600, extract_words=lambda **kwargs: words)

    assert pdf_preprocessor._layout_page_text(page, {}) == (
        "Paper title\nL1\nL2\nL3\nR1\nR2\nR3"
    )


def test_layout_page_text_does_not_split_one_column_text():
    words = []
    for line_index in range(3):
        for word_index in range(7):
            x0 = 50 + word_index * 30
            words.append(
                {
                    "text": f"w{line_index}{word_index}",
                    "x0": x0,
                    "x1": x0 + 20,
                    "top": 100 + line_index * 16,
                    "bottom": 110 + line_index * 16,
                    "size": 10,
                }
            )

    page = SimpleNamespace(width=600, extract_words=lambda **kwargs: words)

    assert pdf_preprocessor._layout_page_text(page, {}) == (
        "w00 w01 w02 w03 w04 w05 w06\n"
        "w10 w11 w12 w13 w14 w15 w16\n"
        "w20 w21 w22 w23 w24 w25 w26"
    )


def test_layout_extraction_falls_back_to_pypdf_for_page_failure(monkeypatch):
    layout_page = SimpleNamespace(
        width=600,
        extract_words=lambda **kwargs: (_ for _ in ()).throw(RuntimeError("broken")),
    )
    fake_pdf = SimpleNamespace(pages=[layout_page])
    pypdf_page = Mock(extract_text=lambda: "Recovered text")
    pypdf_reader = SimpleNamespace(pages=[pypdf_page])

    class FakePdfContext:
        def __enter__(self):
            return fake_pdf

        def __exit__(self, *args):
            return False

    monkeypatch.setattr(pdf_preprocessor.pdfplumber, "open", lambda *_args: FakePdfContext())
    monkeypatch.setattr(pdf_preprocessor, "PdfReader", lambda *_args: pypdf_reader)

    assert pdf_preprocessor._extract_layout_pages(b"pdf", None, {}) == (
        ["Recovered text"],
        1,
    )
