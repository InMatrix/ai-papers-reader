import pytest
from types import SimpleNamespace
from unittest.mock import Mock, patch
from summarize_pdf import clean_markdown_blocks, summarize_pdf, upload_file_with_retry

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
