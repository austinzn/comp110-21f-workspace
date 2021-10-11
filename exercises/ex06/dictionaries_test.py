"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730466197"


def test_dictionaries_regular() -> None:
    """Tests the function using a standard dictionary."""
    assert invert({"a": "b", "f": "g", "t": "r"}) == {'b': 'a', 'g': 'f', 'r': 't'}


def test_dictionaries_blank() -> None:
    """Tests the function using a blank dictionary."""
    assert invert({}) == {}


def test_dictionaries_duplicates() -> None:
    """Tests the function regularly."""
    assert invert({"a": "b", "c": "d"}) == {"b": "a", "d": "c"}


def test_favorite_color_same_max() -> None:
    """Tests the function using two colors tied in frequency."""
    a_dict: dict[str, str] = {"Bryan": "Yellow", "Mark": "Green", "John": "Yellow", "James": "Green"}
    assert favorite_color(a_dict) == "Yellow"


def test_favorite_color_blank() -> None:
    """Tests the function using a blank dictionary."""
    a_dict: dict[str, str] = dict()
    assert favorite_color(a_dict) == ""


def test_favorite_color_regular() -> None:
    """Tests the function using a regular dictionary."""
    a_dict: dict[str, str] = {"Bryan": "Yellow", "Mark": "Green", "John": "Yellow", "James": "Green", "Michael": "Blue", "Timmy": "Green"}
    assert favorite_color(a_dict) == "Green"


def test_count_blank() -> None:
    """Tests the function using a blank dictionary."""
    a_list: list[str] = list()
    assert count(a_list) == {}


def test_count_regular() -> None:
    """Tests the function using a regular list."""
    a_list: list[str] = ["ok", "ok", "ok", "ok", "yes", "yes", "yes", "yes", "hi", "hi"]
    assert count(a_list) == {"ok": 4, "yes": 4, "hi": 2}


def test_count_normal() -> None:
    """Tests the function using a normal list."""
    a_list: list[str] = ["yo", "yo", "yo", "JIIMMMMY Johns", "JIIMMMMY Johns", "JIIMMMMY Johns", "JIIMMMMY Johns", "JIIMMMMY Johns"]
    assert count(a_list) == {"yo": 3, "JIIMMMMY Johns": 5}