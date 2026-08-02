import pytest
from types import SimpleNamespace
from unittest.mock import Mock, patch
from summarize_pdf import (
    clean_markdown_blocks,
    extract_pdf_text,
    find_references_page,
    summarize_pdf,
    upload_file_with_retry,
)

def test_clean_markdown_blocks_with_markers():
    """Test removal of markdown code block markers."""
    input_text = """```markdown
# Title
Some content
```"""
    expected = """# Title
Some content"""
    assert clean_markdown_blocks(input_text) == expected

def test_clean_markdown_blocks_without_markers():
    """Test text without markdown code block markers remains unchanged."""
    input_text = """# Title
Some content"""
    assert clean_markdown_blocks(input_text) == input_text

def test_clean_markdown_blocks_with_extra_whitespace():
    """Test removal of markers with varying whitespace."""
    input_text = """```markdown  
# Title
Some content
```  """
    expected = """# Title
Some content"""
    assert clean_markdown_blocks(input_text) == expected

def test_clean_markdown_blocks_empty_text():
    """Test handling of empty text."""
    assert clean_markdown_blocks("") == ""

def test_upload_file_with_retry_success():
    """Test successful upload on first attempt."""
    mock_file = Mock()
    mock_client = Mock()
    mock_client.files.upload.return_value = mock_file
    
    with patch('summarize_pdf.get_client', return_value=mock_client):
        result = upload_file_with_retry('/tmp/test.pdf', 'test.pdf')
        assert result == mock_file

def test_upload_file_with_retry_success_after_failure():
    """Test successful upload after one failure."""
    mock_file = Mock()
    
    # Create a mock error with '503' in the message
    mock_error = Exception("503 Service Unavailable")
    
    mock_client = Mock()
    mock_upload = mock_client.files.upload
    # First call raises 503, second call succeeds
    mock_upload.side_effect = [mock_error, mock_file]
    
    with patch('summarize_pdf.get_client', return_value=mock_client):
        with patch('time.sleep'):  # Mock sleep to speed up test
            result = upload_file_with_retry('/tmp/test.pdf', 'test.pdf', max_retries=3)
            assert result == mock_file
            assert mock_upload.call_count == 2

def test_upload_file_with_retry_max_retries_exceeded():
    """Test that exception is raised after max retries."""
    mock_error = Exception("503 Service Unavailable")
    
    mock_client = Mock()
    mock_client.files.upload.side_effect = mock_error
    
    with patch('summarize_pdf.get_client', return_value=mock_client):
        with patch('time.sleep'):  # Mock sleep to speed up test
            with pytest.raises(Exception):
                upload_file_with_retry('/tmp/test.pdf', 'test.pdf', max_retries=3)

def test_upload_file_with_retry_non_retryable_error():
    """Test that non-retryable errors are raised immediately."""
    mock_error = Exception("404 Not Found")
    
    mock_client = Mock()
    mock_client.files.upload.side_effect = mock_error
    
    with patch('summarize_pdf.get_client', return_value=mock_client):
        with pytest.raises(Exception):
            upload_file_with_retry('/tmp/test.pdf', 'test.pdf', max_retries=3)


def test_summarize_pdf_with_deepseek_extracts_text():
    mock_client = Mock()
    mock_client.chat.completions.create.return_value = SimpleNamespace(
        choices=[
            SimpleNamespace(
                message=SimpleNamespace(content="# Summary\nPaper summary")
            )
        ]
    )

    with patch("summarize_pdf.extract_pdf_text", return_value="Extracted paper text"):
        result = summarize_pdf(
            b"pdf content",
            client=mock_client,
            provider="deepseek",
            model="deepseek-v4-flash",
        )

    assert result == "# Summary\nPaper summary"
    request = mock_client.chat.completions.create.call_args.kwargs
    assert request["model"] == "deepseek-v4-flash"
    assert "<paper>\nExtracted paper text\n</paper>" in request["messages"][0]["content"]


def test_extract_pdf_text_limits_pages(monkeypatch):
    import summarize_pdf

    pages = [Mock(extract_text=lambda i=i: f"Page {i}") for i in range(3)]
    reader = Mock(pages=pages)
    monkeypatch.setattr(summarize_pdf, "PdfReader", Mock(return_value=reader))

    assert summarize_pdf.extract_pdf_text(b"pdf", max_pages=2) == "Page 0\n\nPage 1"


def test_find_references_page_detects_numbered_heading(monkeypatch):
    import summarize_pdf

    pages = [
        Mock(extract_text=lambda: "5 Methods\nDetails"),
        Mock(extract_text=lambda: "6. References\n[1] A paper"),
    ]
    reader = Mock(pages=pages)
    monkeypatch.setattr(summarize_pdf, "load_config", lambda: {"pdf": {}})

    assert find_references_page(reader) == 1


def test_extract_pdf_text_stops_before_references(monkeypatch):
    import summarize_pdf

    pages = [
        Mock(extract_text=lambda: "Introduction\nBody"),
        Mock(extract_text=lambda: "Conclusion\nReferences\n[1] A paper"),
        Mock(extract_text=lambda: "[2] Another paper"),
    ]
    reader = Mock(pages=pages)
    monkeypatch.setattr(summarize_pdf, "PdfReader", Mock(return_value=reader))
    monkeypatch.setattr(
        summarize_pdf,
        "load_config",
        lambda: {"pdf": {"max_bytes": 3, "stop_at_references": True}},
    )

    assert extract_pdf_text(b"large") == "Introduction\nBody\n\nConclusion"


def test_extract_pdf_text_keeps_references_for_small_documents(monkeypatch):
    import summarize_pdf

    pages = [
        Mock(extract_text=lambda: "Introduction\nBody"),
        Mock(extract_text=lambda: "Conclusion\nReferences\n[1] A paper"),
    ]
    reader = Mock(pages=pages)
    monkeypatch.setattr(summarize_pdf, "PdfReader", Mock(return_value=reader))
    monkeypatch.setattr(
        summarize_pdf,
        "load_config",
        lambda: {"pdf": {"max_bytes": 100, "stop_at_references": True}},
    )

    assert extract_pdf_text(b"small") == (
        "Introduction\nBody\n\nConclusion\nReferences\n[1] A paper"
    )


def test_extract_pdf_text_caps_only_oversized_documents(monkeypatch):
    import summarize_pdf

    pages = [Mock(extract_text=lambda i=i: f"Page {i}") for i in range(3)]
    reader = Mock(pages=pages)
    monkeypatch.setattr(summarize_pdf, "PdfReader", Mock(return_value=reader))
    monkeypatch.setattr(
        summarize_pdf,
        "load_config",
        lambda: {"pdf": {"max_pages": 2, "max_bytes": 3, "stop_at_references": False}},
    )

    assert extract_pdf_text(b"large") == "Page 0\n\nPage 1"


def test_truncate_pdf_prefers_body_before_references(monkeypatch):
    import summarize_pdf

    pages = [
        Mock(extract_text=lambda: "Introduction"),
        Mock(extract_text=lambda: "References\n[1] A paper"),
        Mock(extract_text=lambda: "[2] Another paper"),
    ]
    reader = Mock(pages=pages)

    class FakeWriter:
        instances = []

        def __init__(self):
            self.pages = []
            FakeWriter.instances.append(self)

        def add_page(self, page):
            self.pages.append(page)

        def write(self, stream):
            stream.write(b"x" * len(self.pages))

    monkeypatch.setattr(summarize_pdf, "PdfReader", Mock(return_value=reader))
    monkeypatch.setattr(summarize_pdf, "PdfWriter", FakeWriter)
    monkeypatch.setattr(
        summarize_pdf,
        "load_config",
        lambda: {"pdf": {"max_bytes": 1, "max_pages": 12}},
    )

    assert summarize_pdf.truncate_pdf(b"large", max_bytes=1) == b"x"
    assert [len(writer.pages) for writer in FakeWriter.instances] == [1]


def test_truncate_pdf_keeps_small_documents(monkeypatch):
    import importlib

    summarize_pdf_module = importlib.import_module("summarize_pdf")
    assert summarize_pdf_module.truncate_pdf(b"small", max_bytes=10) == b"small"


def test_truncate_pdf_limits_large_documents(monkeypatch):
    import importlib

    summarize_pdf_module = importlib.import_module("summarize_pdf")

    pages = [Mock() for _ in range(3)]
    reader = Mock(pages=pages)
    writer = Mock()
    output = Mock()
    output.getvalue.return_value = b"first pages"
    writer.write.side_effect = lambda stream: None
    monkeypatch.setattr(summarize_pdf_module, "PdfReader", Mock(return_value=reader))
    monkeypatch.setattr(summarize_pdf_module, "PdfWriter", Mock(return_value=writer))
    monkeypatch.setattr(summarize_pdf_module, "BytesIO", Mock(return_value=output))

    assert summarize_pdf_module.truncate_pdf(
        b"large", max_pages=2, max_bytes=1
    ) == b"first pages"
    assert writer.add_page.call_count == 2
