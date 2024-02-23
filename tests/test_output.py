from unittest.mock import patch, mock_open
import pytest
from sentiment.output import OutputHandler

@pytest.fixture
def output_handler():
    return OutputHandler()

def test_empty_output_filepath():
    output = OutputHandler()
    assert output.output_filepath == None

def test_output_filepath():
    filepath = 'File.txt'
    output = OutputHandler(output_filepath=filepath)
    assert output.output_filepath == filepath

def test_output_handler_print_sentiment_score_invalid_type(output_handler):
    with pytest.raises(Exception):
        output_handler.print_sentiment_score('Wrong type')

def test_print_to_file_correctly(output_handler):
    output_filepath = 'output_filepath.txt'
    text = "This is a test sentence."
    
    with patch("builtins.open", mock_open()) as mock_file_open:
        output_handler._print_to_file(text, output_filepath)
        mock_file_open.assert_called_once_with(output_filepath, "a+")
        mock_file_open().write.assert_called_once_with(text)

def test_print_to_file_invalid_type(output_handler):
    wrong_type = {}
    correct_type = 'This is a test sentence.'
    with pytest.raises(TypeError):
        output_handler._print_to_file(wrong_type, correct_type)
    with pytest.raises(TypeError):
        output_handler._print_to_file(correct_type, wrong_type)
    with pytest.raises(TypeError):
        output_handler._print_to_file(wrong_type, wrong_type)

def test_print_to_console_correctly(output_handler, capsys):
    text = "This is a test sentence."
    output_handler._print_to_console(text)
    captured = capsys.readouterr()
    assert captured.out == text + '\n'

def test_print_to_console_invalid_type(output_handler):
    wrong_type = {"const1": 'const2'}
    with pytest.raises(TypeError):
        output_handler._print_to_console(wrong_type)
    