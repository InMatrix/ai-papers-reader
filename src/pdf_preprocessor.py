"""Download and preprocess PDFs locally before sending content to an LLM."""

import re
import time
from io import BytesIO

import requests
from pypdf import PdfReader, PdfWriter

from llm_client import load_config


DEFAULT_MAX_PAGES = 12
DEFAULT_MAX_BYTES = 15 * 1024 * 1024
DEFAULT_REFERENCE_HEADINGS = ("references", "bibliography", "works cited")
DEFAULT_CONNECT_TIMEOUT_SECONDS = 20
DEFAULT_READ_TIMEOUT_SECONDS = 120
DEFAULT_DOWNLOAD_RETRIES = 4
DEFAULT_DOWNLOAD_BACKOFF_SECONDS = 2
DEFAULT_DOWNLOAD_CHUNK_SIZE_BYTES = 1024 * 1024
RETRYABLE_HTTP_STATUSES = {408, 425, 429, 500, 502, 503, 504}


class PdfDownloadError(RuntimeError):
    """Raised when a PDF cannot be downloaded after all retry attempts."""


def _pdf_config(config=None):
    """Return the PDF configuration as a mapping."""
    config = config if config is not None else load_config()
    pdf_config = config.get("pdf", {}) or {}
    if not isinstance(pdf_config, dict):
        raise ValueError("The pdf config must be a YAML mapping")
    return pdf_config


def _download_settings(pdf_config):
    """Resolve and validate download timeout/retry settings."""
    legacy_timeout = float(
        pdf_config.get("download_timeout_seconds", DEFAULT_READ_TIMEOUT_SECONDS)
    )
    connect_timeout = float(
        pdf_config.get(
            "download_connect_timeout_seconds",
            min(DEFAULT_CONNECT_TIMEOUT_SECONDS, legacy_timeout),
        )
    )
    read_timeout = float(
        pdf_config.get("download_read_timeout_seconds", legacy_timeout)
    )
    retries = int(pdf_config.get("download_retries", DEFAULT_DOWNLOAD_RETRIES))
    backoff = float(
        pdf_config.get(
            "download_retry_backoff_seconds", DEFAULT_DOWNLOAD_BACKOFF_SECONDS
        )
    )
    chunk_size = int(
        pdf_config.get(
            "download_chunk_size_bytes", DEFAULT_DOWNLOAD_CHUNK_SIZE_BYTES
        )
    )

    if connect_timeout <= 0 or read_timeout <= 0:
        raise ValueError("PDF download timeouts must be greater than 0")
    if retries < 0:
        raise ValueError("pdf.download_retries must be at least 0")
    if backoff < 0:
        raise ValueError("pdf.download_retry_backoff_seconds cannot be negative")
    if chunk_size < 1:
        raise ValueError("pdf.download_chunk_size_bytes must be at least 1")

    return connect_timeout, read_timeout, retries, backoff, chunk_size


def _is_retryable_http_error(error):
    """Return whether an HTTP error represents a transient response."""
    response = getattr(error, "response", None)
    return getattr(response, "status_code", None) in RETRYABLE_HTTP_STATUSES


def download_pdf(url, session=None):
    """Download a PDF with streaming, bounded timeouts, and exponential retries."""
    pdf_config = _pdf_config()
    (
        connect_timeout,
        read_timeout,
        retries,
        backoff,
        chunk_size,
    ) = _download_settings(pdf_config)

    client = session if session is not None else requests.Session()
    last_error = None
    content = bytearray()
    try:
        for attempt in range(retries + 1):
            response = None
            try:
                headers = {"Accept": "application/pdf"}
                if content:
                    headers["Range"] = f"bytes={len(content)}-"
                response = client.get(
                    url,
                    headers=headers,
                    stream=True,
                    timeout=(connect_timeout, read_timeout),
                )
                response.raise_for_status()
                # Some servers ignore Range and return the complete document;
                # replace the partial buffer rather than duplicating bytes.
                if content and response.status_code == 200:
                    content.clear()
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        content.extend(chunk)
                if not content:
                    raise PdfDownloadError("Downloaded PDF is empty")
                if attempt:
                    print(f"Downloaded PDF after {attempt + 1} attempt(s)")
                return bytes(content)
            except requests.HTTPError as error:
                if not _is_retryable_http_error(error):
                    raise
                last_error = error
            except (requests.RequestException, PdfDownloadError, OSError) as error:
                last_error = error
            finally:
                if response is not None:
                    response.close()

            if attempt >= retries:
                break
            delay = backoff * (2**attempt)
            print(
                f"PDF download attempt {attempt + 1} failed: {last_error}. "
                f"Retrying in {delay:g} seconds..."
            )
            time.sleep(delay)
    finally:
        if session is None:
            client.close()

    raise PdfDownloadError(
        f"Failed to download PDF after {retries + 1} attempt(s): {last_error}"
    ) from last_error


def _reference_headings(pdf_config):
    """Return normalized section names that indicate the references section."""
    headings = pdf_config.get("references_headings", DEFAULT_REFERENCE_HEADINGS)
    if isinstance(headings, str):
        headings = [headings]
    if not isinstance(headings, (list, tuple, set)):
        raise ValueError("pdf.references_headings must be a list of strings")
    return {
        re.sub(r"\s+", " ", str(heading)).strip().casefold()
        for heading in headings
        if str(heading).strip()
    }


def _normalize_heading(line):
    """Normalize a PDF text line for section-heading matching."""
    line = re.sub(r"\s+", " ", line).strip()
    # Academic papers commonly number this section as "6 References" or
    # "6. References". Roman numeral prefixes are supported as well.
    line = re.sub(
        r"^(?:(?:\d+(?:\.\d+)*)|(?:[IVXLCDM]+))[.)]?\s+",
        "",
        line,
        flags=re.IGNORECASE,
    )
    return line.rstrip(":").strip().casefold()


def _reference_heading_position(text, headings):
    """Return the character offset of a references heading, if present."""
    offset = 0
    for line in text.splitlines(keepends=True):
        if _normalize_heading(line.rstrip("\r\n")) in headings:
            return offset
        offset += len(line)
    return None


def _page_text(page):
    """Extract text from one page, treating malformed/scanned pages as empty."""
    try:
        text = page.extract_text() or ""
    except Exception as error:
        print(f"Unable to extract text from PDF page: {error}")
        return ""
    return text if isinstance(text, str) else ""


def find_references_page(reader, pdf_config=None):
    """Return the zero-based page containing a References-style heading."""
    if pdf_config is None:
        pdf_config = _pdf_config()
    elif not isinstance(pdf_config, dict):
        raise ValueError("The pdf config must be a YAML mapping")
    elif "pdf" in pdf_config:
        pdf_config = _pdf_config(pdf_config)
    if not pdf_config.get("stop_at_references", True):
        return None

    headings = _reference_headings(pdf_config)
    if not headings:
        return None

    for page_number, page in enumerate(reader.pages):
        if _reference_heading_position(_page_text(page), headings) is not None:
            return page_number
    return None


def _write_pdf_pages(reader, page_count):
    """Create a PDF containing the first ``page_count`` pages."""
    writer = PdfWriter()
    for page in reader.pages[:page_count]:
        writer.add_page(page)

    output = BytesIO()
    writer.write(output)
    return output.getvalue()


def _fit_pdf_to_byte_limit(reader, max_pages, max_bytes):
    """Keep dropping trailing pages until the generated PDF fits the cap."""
    page_count = min(max_pages, len(reader.pages))
    if page_count == 0:
        return b"", 0
    last_content = None
    for kept_pages in range(page_count, 0, -1):
        candidate = _write_pdf_pages(reader, kept_pages)
        last_content = candidate
        if len(candidate) <= max_bytes:
            return candidate, kept_pages

    # A single page can itself exceed the configured cap. It is still the
    # smallest useful document and is preferable to returning no PDF at all.
    return last_content, 1


def extract_pdf_text(pdf_content, max_pages=None, max_bytes=None):
    """Extract full text below the byte cap; trim oversized papers safely."""
    pdf_config = _pdf_config()
    max_pages_was_explicit = max_pages is not None
    if max_pages is None:
        max_pages = int(pdf_config.get("max_pages", DEFAULT_MAX_PAGES))
    if max_pages < 1:
        raise ValueError("pdf.max_pages must be at least 1")
    if max_bytes is None:
        max_bytes = int(pdf_config.get("max_bytes", DEFAULT_MAX_BYTES))
    if max_bytes < 1:
        raise ValueError("pdf.max_bytes must be at least 1")

    reader = PdfReader(BytesIO(pdf_content))
    page_count = len(reader.pages)
    # An explicit function argument remains a deliberate one-off cap. The
    # committed config cap only applies to oversized PDFs, as documented.
    page_limit = page_count
    if max_pages_was_explicit or len(pdf_content) > max_bytes:
        page_limit = min(page_limit, max_pages)

    oversized = len(pdf_content) > max_bytes
    headings = _reference_headings(pdf_config) if oversized else set()
    extracted_pages = []
    references_found = False
    for page_number, page in enumerate(reader.pages[:page_limit]):
        page_text = _page_text(page)
        heading_position = None
        if oversized and pdf_config.get("stop_at_references", True) and headings:
            heading_position = _reference_heading_position(page_text, headings)
        if heading_position is not None:
            # Preserve an introduction or conclusion that shares a page with
            # the heading, while excluding the references themselves.
            page_text = page_text[:heading_position]
            references_found = True
        if page_text.strip():
            extracted_pages.append(page_text.strip())
        if heading_position is not None:
            break

    if references_found:
        print(f"Stopping PDF text extraction before References on page {page_number + 1}")
    elif page_limit < page_count:
        print(f"Limiting PDF text input to the first {page_limit} pages")

    text = "\n\n".join(extracted_pages).strip()
    if not text:
        raise ValueError("No text could be extracted from the PDF")
    return text


def truncate_pdf(pdf_content, max_pages=None, max_bytes=None):
    """Remove references and apply size/page limits when needed."""
    pdf_config = _pdf_config()
    if max_bytes is None:
        max_bytes = int(pdf_config.get("max_bytes", DEFAULT_MAX_BYTES))
    if max_bytes < 1:
        raise ValueError("pdf.max_bytes must be at least 1")
    if max_pages is None:
        max_pages = int(pdf_config.get("max_pages", DEFAULT_MAX_PAGES))
    if max_pages < 1:
        raise ValueError("pdf.max_pages must be at least 1")

    oversized = len(pdf_content) > max_bytes
    if not oversized:
        return pdf_content

    reader = PdfReader(BytesIO(pdf_content))
    references_page = find_references_page(reader, pdf_config)

    # Prefer the complete paper body when a References heading is detected.
    # If that still exceeds the byte cap, fall back to the configured hard
    # page limit. A heading on page zero cannot be represented without
    # rewriting page content, so it uses the same safe fallback.
    if references_page is not None and references_page > 0:
        body_content = _write_pdf_pages(reader, references_page)
        if len(body_content) <= max_bytes:
            print(
                f"PDF is {len(pdf_content)} bytes; excluding References and "
                f"keeping the first {references_page} pages ({len(body_content)} bytes)"
            )
            return body_content
        print(
            f"The pre-References PDF is {len(body_content)} bytes; "
            f"applying the {max_pages}-page fallback"
        )

    truncated_content, kept_pages = _fit_pdf_to_byte_limit(
        reader, max_pages, max_bytes
    )
    if len(truncated_content) <= max_bytes:
        print(
            f"PDF is {len(pdf_content)} bytes; limiting Gemini input to the first "
            f"{kept_pages} pages ({len(truncated_content)} bytes)"
        )
    else:
        print(
            f"Even the first page is {len(truncated_content)} bytes, above the "
            f"{max_bytes}-byte limit; keeping the smallest available PDF"
        )
    return truncated_content
