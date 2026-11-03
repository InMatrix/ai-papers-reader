from io import BytesIO
from unittest.mock import Mock, patch

import pytest
import requests
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    DictionaryObject,
    IndirectObject,
    NameObject,
    RectangleObject,
    TextStringObject,
)

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


def pdf_with_indirect_mediabox_and_named_link():
    """Build three pages shaped like the arXiv papers that crashed pypdf."""
    writer = PdfWriter()
    for _ in range(3):
        writer.add_blank_page(width=612, height=792)
    writer.add_named_destination("section.1", 1)
    writer.add_annotation(
        0,
        DictionaryObject(
            {
                NameObject("/Type"): NameObject("/Annot"),
                NameObject("/Subtype"): NameObject("/Link"),
                NameObject("/Rect"): RectangleObject((0, 0, 10, 10)),
                NameObject("/Dest"): TextStringObject("section.1"),
            }
        ),
    )
    for page in writer.pages:
        page[NameObject("/MediaBox")] = writer._add_object(page.mediabox)

    output = BytesIO()
    writer.write(output)
    return output.getvalue()


def test_truncate_pdf_main_text_only_handles_indirect_mediabox_with_named_links(
    monkeypatch,
):
    pdf_content = pdf_with_indirect_mediabox_and_named_link()
    assert isinstance(
        PdfReader(BytesIO(pdf_content)).pages[0].raw_get("/MediaBox"), IndirectObject
    )
    monkeypatch.setattr(
        pdf_preprocessor, "load_config", lambda: {"pdf": {"max_bytes": 1024 * 1024}}
    )
    # These blank pages have no References heading to find.
    monkeypatch.setattr(pdf_preprocessor, "find_references_page", lambda *args: 1)

    # Resolving the link used to raise "object of type 'IndirectObject' has no len()".
    trimmed = pdf_preprocessor.truncate_pdf(pdf_content, main_text_only=True)

    assert len(PdfReader(BytesIO(trimmed)).pages) == 2


def numbered_pdf(page_count):
    """Build blank pages whose widths record their position in the document."""
    writer = PdfWriter()
    for page_number in range(page_count):
        writer.add_blank_page(width=100 + page_number, height=100)

    output = BytesIO()
    writer.write(output)
    return output.getvalue()


def page_numbers(pdf_content):
    """Read back the original position of each page from a numbered_pdf."""
    return [
        int(page.mediabox.width) - 100 for page in PdfReader(BytesIO(pdf_content)).pages
    ]


def use_page_cap(
    monkeypatch, max_main_text_pages=6, main_text_tail_pages=2, max_bytes=1024 * 1024
):
    monkeypatch.setattr(
        pdf_preprocessor,
        "load_config",
        lambda: {
            "pdf": {
                "max_main_text_pages": max_main_text_pages,
                "main_text_tail_pages": main_text_tail_pages,
                "max_bytes": max_bytes,
            }
        },
    )


def test_cap_main_text_pages_keeps_first_and_last_pages_through_references(monkeypatch):
    use_page_cap(monkeypatch)
    monkeypatch.setattr(pdf_preprocessor, "find_references_page", lambda *args: 9)

    excerpt, description = pdf_preprocessor.cap_main_text_pages(numbered_pdf(12))

    assert page_numbers(excerpt) == [0, 1, 2, 3, 8, 9]
    assert description == "the first 4 and last 2 of its 10 main-text pages"


# A heading on page zero leaves no main text to measure, so truncate_pdf ignores
# it too.
@pytest.mark.parametrize("references_page", [None, 0])
def test_cap_main_text_pages_counts_every_page_without_a_usable_heading(
    monkeypatch, references_page
):
    use_page_cap(monkeypatch)
    monkeypatch.setattr(
        pdf_preprocessor, "find_references_page", lambda *args: references_page
    )

    excerpt, description = pdf_preprocessor.cap_main_text_pages(numbered_pdf(8))

    assert page_numbers(excerpt) == [0, 1, 2, 3, 6, 7]
    assert description == "the first 4 and last 2 of its 8 main-text pages"


def test_cap_main_text_pages_ignores_pages_after_references(monkeypatch):
    use_page_cap(monkeypatch)
    monkeypatch.setattr(pdf_preprocessor, "find_references_page", lambda *args: 5)
    pdf_content = numbered_pdf(40)

    assert pdf_preprocessor.cap_main_text_pages(pdf_content) == (pdf_content, None)


def test_cap_main_text_pages_keeps_a_paper_at_the_limit(monkeypatch):
    use_page_cap(monkeypatch)
    pdf_content = numbered_pdf(6)

    assert pdf_preprocessor.cap_main_text_pages(pdf_content) == (pdf_content, None)


@pytest.mark.parametrize("main_text_tail_pages", [0, 6])
def test_cap_main_text_pages_rejects_a_tail_that_leaves_no_first_pages_or_no_last_pages(
    monkeypatch, main_text_tail_pages
):
    use_page_cap(monkeypatch, main_text_tail_pages=main_text_tail_pages)

    with pytest.raises(ValueError, match="main_text_tail_pages"):
        pdf_preprocessor.cap_main_text_pages(numbered_pdf(8))


# Writing one byte per page turns the byte limit into a page limit.
@pytest.mark.parametrize(
    "max_bytes, kept_pages, description",
    [
        (4, [0, 1, 6, 7], "the first 2 and last 2 of its 8 main-text pages"),
        (2, [0, 7], "the first 1 and last 1 of its 8 main-text pages"),
    ],
)
def test_cap_main_text_pages_fits_the_byte_limit_by_dropping_first_pages_before_last(
    monkeypatch, max_bytes, kept_pages, description
):
    use_page_cap(monkeypatch, max_bytes=max_bytes)
    written = []

    def write_one_byte_per_page(reader, page_numbers):
        written.append(list(page_numbers))
        return b"x" * len(written[-1])

    monkeypatch.setattr(pdf_preprocessor, "_write_pdf_pages", write_one_byte_per_page)

    excerpt, actual_description = pdf_preprocessor.cap_main_text_pages(numbered_pdf(8))

    assert written[-1] == kept_pages
    assert len(excerpt) == len(kept_pages)
    assert actual_description == description


def test_cap_main_text_pages_stops_at_one_page_when_nothing_fits_the_byte_limit(
    monkeypatch,
):
    use_page_cap(monkeypatch, max_bytes=1)
    monkeypatch.setattr(
        pdf_preprocessor, "_write_pdf_pages", lambda reader, page_numbers: b"too large"
    )

    _, description = pdf_preprocessor.cap_main_text_pages(numbered_pdf(8))

    assert description == "the first 1 and last 0 of its 8 main-text pages"


def test_cap_main_text_pages_excerpt_is_not_cut_again_by_truncate_pdf(monkeypatch):
    use_page_cap(monkeypatch, max_bytes=len(numbered_pdf(5)))

    excerpt, _ = pdf_preprocessor.cap_main_text_pages(numbered_pdf(8))

    assert page_numbers(excerpt)[-2:] == [6, 7]
    assert pdf_preprocessor.truncate_pdf(excerpt, main_text_only=True) == excerpt
