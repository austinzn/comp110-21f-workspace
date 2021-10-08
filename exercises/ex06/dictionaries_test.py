"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730466197"

def test_dictionaries_regular() -> None:
    assert invert({"a": "b", "f": "g", "t": "r"}) == {'b': 'a', 'g': 'f', 'r': 't'}