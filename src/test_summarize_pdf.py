import pytest
from unittest.mock import Mock, patch
from summarize_pdf import clean_markdown_blocks, upload_file_with_retry

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
    with patch('summarize_pdf.client.files.upload', return_value=mock_file):
        result = upload_file_with_retry('/tmp/test.pdf', 'test.pdf')
        assert result == mock_file

def test_upload_file_with_retry_success_after_failure():
    """Test successful upload after one failure."""
    from googleapiclient.errors import HttpError
    
    mock_file = Mock()
    mock_resp = Mock()
    mock_resp.status = 503
    
    # Create a mock HttpError
    http_error = HttpError(mock_resp, b'Service Unavailable')
    
    with patch('summarize_pdf.client.files.upload') as mock_upload:
        # First call raises 503, second call succeeds
        mock_upload.side_effect = [http_error, mock_file]
        
        with patch('time.sleep'):  # Mock sleep to speed up test
            result = upload_file_with_retry('/tmp/test.pdf', 'test.pdf', max_retries=3)
            assert result == mock_file
            assert mock_upload.call_count == 2

def test_upload_file_with_retry_max_retries_exceeded():
    """Test that exception is raised after max retries."""
    from googleapiclient.errors import HttpError
    
    mock_resp = Mock()
    mock_resp.status = 503
    http_error = HttpError(mock_resp, b'Service Unavailable')
    
    with patch('summarize_pdf.client.files.upload', side_effect=http_error):
        with patch('time.sleep'):  # Mock sleep to speed up test
            with pytest.raises(HttpError):
                upload_file_with_retry('/tmp/test.pdf', 'test.pdf', max_retries=3)

def test_upload_file_with_retry_non_retryable_error():
    """Test that non-retryable errors are raised immediately."""
    from googleapiclient.errors import HttpError
    
    mock_resp = Mock()
    mock_resp.status = 404  # Not Found - not retryable
    http_error = HttpError(mock_resp, b'Not Found')
    
    with patch('summarize_pdf.client.files.upload', side_effect=http_error):
        with pytest.raises(HttpError):
            result = upload_file_with_retry('/tmp/test.pdf', 'test.pdf', max_retries=3)