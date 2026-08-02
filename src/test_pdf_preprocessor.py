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
