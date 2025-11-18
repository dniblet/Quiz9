# analyzer.py

import re
from collections import Counter

def count_words(text: str) -> int:
    """Return number of words in text. Words are sequences of alphanumeric chars."""
    if not text:
        return 0
    words = re.findall(r"[A-Za-z0-9']+", text)
    return len(words)

def count_chars(text: str) -> int:
    """Return number of characters including spaces."""
    if text is None:
        return 0
    return len(text)

def find_most_common_word(text: str):
    """Return the most common word in text. Case-insensitive. Returns None if no words."""
    if not text:
        return None
    words = re.findall(r"[A-Za-z0-9']+", text.lower())
    if not words:
        return None
    counter = Counter(words)
    return counter.most_common(1)[0]

if __name__ == "__main__":
    # simple manual tests
    samples = [
        "",
        "Hello world!",
        "Hello, hello... HELLO!!!",
        "Punctuation: does it count? Yes, it does!",
    ]
    for s in samples:
        print("Text:", repr(s))
        print("Words:", count_words(s))
        print("Chars:", count_chars(s))
        print("Most common:", find_most_common_word(s))
        print()
