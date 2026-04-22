"""Starter test. Add more as you learn pytest."""
from learning.example import chunked, greet


def test_greet_returns_greeting():
    assert greet("Ada") == "Hello, Ada!"


def test_chunked_splits_evenly():
    assert chunked([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
