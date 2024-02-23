import argparse
import logging

logger = logging.getLogger(__name__)


class UnsupportedFileTypeException(Exception):
    pass

def parse_args():
    ap = argparse.ArgumentParser(allow_abbrev=False)
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-f",
        "--filepath",
        type=str,
        help="Request filepath in .txt format",
    )
    group.add_argument(
        "-t",
        "--text",
        type=str,
        help="Request text",
    )
    ap.add_argument(
        "-o", 
        "--output_file", 
        type=str,
        required=False,
        help="Path to the output text file (optional)."
    )
    return ap.parse_args()

def read_text(filepath: str, text: str) -> str:
    if filepath:
        if filepath.endswith(".txt"):
            try:
                with open(filepath, "r") as file:
                    output = file.read()
            except FileNotFoundError as e:
                logger.error(f"File '{filepath}' not found.")
                raise 
        else:
            logger.error('Wrong file extension')
            raise UnsupportedFileTypeException(filepath)
    elif text:
        output = text
    else:
        logger.error('Error occured during reading text')
        raise ValueError

    if output.strip():
        return output
    else:
        logger.error('Text is empty')
        raise ValueError
