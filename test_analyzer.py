

import pytest
from analyzer import count_words, count_chars, find_most_common_word

def test_count_words_empty():
    assert count_words("") == 0

def test_count_words_simple():
    assert count_words("hello world") == 2

def test_count_words_punctuation():
    assert count_words("Hello, world! This... works?") == 4

def test_count_chars_empty():
    assert count_chars("") == 0

def test_count_chars_spaces():
    assert count_chars("a b c") == 5

def test_most_common_word_basic():
    assert find_most_common_word("cat dog cat") == ("cat", 2)

def test_most_common_word_case_insensitive():
    assert find_most_common_word("Hello hello HELLO") == ("hello", 3)

def test_most_common_word_none():
    assert find_most_common_word("!!! ??? ...") is None
