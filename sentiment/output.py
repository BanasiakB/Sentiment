from typing import Optional
import logging

class OutputHandler:
    def __init__(self, output_filepath: Optional[str] = None):
        self.output_filepath = output_filepath
        self.logger = logging.getLogger(__name__)

    def print_sentiment_score(self, sentiment_score: dict) -> None:
        try:
            output_text = f"Sentiment Analysis Result:\nLabel: {sentiment_score['label']}\nScore: {sentiment_score['score']}\n"
            
            if self.output_filepath:
                self._print_to_file(output_text, self.output_filepath)
            else:
                self._print_to_console(output_text)
            
        except Exception as e:
            self.logger.error(f"Error occurred while printing sentiment score: {e}")
            raise

    def _print_to_console(self, text: str) -> None:
        if type(text) is str:
            try:
                print(text)
            except Exception as e:
                self.logger.error(f"Error occurred while printing: {e}")
                raise
        else:
            self.logger.error("Wrong type of input.")
            raise TypeError('Wrong type of input')


    def _print_to_file(self, text: str, output_filepath: str) -> None:
        if type(text) is not str or type(output_filepath) is not str:
            self.logger.error("Wrong type of inputs.")
            raise TypeError('Wrong type of inputs.')
        try:
            with open(output_filepath, "a+") as f:
                f.write(text)
        except Exception as e:
            self.logger.error(f"Error occurred while writing to file: {e}")
