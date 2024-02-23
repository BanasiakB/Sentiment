from silence_tensorflow import silence_tensorflow
from transformers import pipeline
import logging

class SentimentAnalyzer:
    def __init__(self):
        silence_tensorflow()
        self.sentiment_pipeline = pipeline("sentiment-analysis", model='distilbert/distilbert-base-uncased-finetuned-sst-2-english')
        self.logger = logging.getLogger(type(self).__name__)

    def analyze_sentiment(self, text: str) -> dict:
        if type(text) is not str:
            self.logger.error("Wrong type of text.")
            raise TypeError('Wrong type of text.')
        try:
            return self.sentiment_pipeline(text)[0]        
        except Exception as e:
            self.logger.error(f"Error occurred during sentiment analysis: {e}")
            raise 
