from unittest.mock import patch, mock_open
import pytest
from sentiment.reader import UnsupportedFileTypeException, read_text

def test_read_file():
    file_content = "This is a test sentence from a file."
    with patch("builtins.open", mock_open(read_data=file_content)):
        output = read_text("test_file.txt", None)
    assert output == file_content

def test_read_empty_file():
    with pytest.raises(ValueError):
        file_content = ""
        with patch("builtins.open", mock_open(read_data=file_content)):
            read_text("empty_test_file.txt", None)

def test_wrong_file():
    with pytest.raises(UnsupportedFileTypeException):
        file_content = "This is a test sentence from a file."
        with patch("builtins.open", mock_open(read_data=file_content)):
            read_text("wrong_extension_file.pdf", None)

def test_read_file_invalid_filpath():
    with pytest.raises(FileNotFoundError):
        read_text("nonexistent_file.txt", None)

def test_read_text():
    text = "This is a test sentence"
    assert read_text(None, text) == text

def test_read_empty_text():
    with pytest.raises(ValueError):
        text = ""
        read_text(None, text)

def test_read_nothing():
    with pytest.raises(ValueError):
        read_text(None, None)



