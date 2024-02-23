from log import setup_log
from reader import parse_args, read_text
from output import OutputHandler
from model import SentimentAnalyzer

def main():
    setup_log()
    args = parse_args()
    text = read_text(args.filepath, args.text)
    sentiment_score = SentimentAnalyzer().analyze_sentiment(text)
    OutputHandler(args.output_file).print_sentiment_score(sentiment_score)

if __name__ == "__main__":
    main()
