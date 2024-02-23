import pytest
from sentiment.model import SentimentAnalyzer

@pytest.fixture
def analyzer():
    return SentimentAnalyzer()


def test_analyze_sentiment(analyzer):
    text = "This is a test sentence."
    sentiment_score = analyzer.analyze_sentiment(text)
    assert 'label' in sentiment_score
    assert 'score' in sentiment_score

def test_analyze_sentiment_wrong_input(analyzer):
    with pytest.raises(TypeError):
        wrong_type = []
        analyzer.analyze_sentiment(wrong_type)

def test_analyze_sentiment_no_input(analyzer):
    with pytest.raises(TypeError):
        analyzer.analyze_sentiment(None)
