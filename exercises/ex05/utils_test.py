"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730466197"


def test_only_evens_regular() -> None:
    """Tests if the function works with a basic list."""
    a_list: list[int] = [1, 2, 3]
    assert only_evens(a_list) == [2]


def test_only_evens_blank() -> None:
    """Tests if the function works with a blank list."""
    a_list: list[int] = list()
    assert only_evens(a_list) == []


def test_only_evens_same() -> None:
    """Tests if the function works with multiple of the same number."""
    a_list: list[int] = [4, 4, 4]
    assert only_evens(a_list) == [4, 4, 4]


def test_sub_blank() -> None:
    """Tests the function with a blank list."""
    a_list: list[int] = list()
    assert sub(a_list, 0, 3) == []


def test_sub_over() -> None:
    """Tests when the function parameter goes over."""
    a_list: list[int] = [1, 2, 3, 4]
    assert sub(a_list, 1, 5) == [2, 3, 4]


def test_sub_under() -> None:
    """Tests the function with a negative parameter."""
    a_list: list[int] = [1, 2, 3, 4]
    assert sub(a_list, -1, 3) == [1, 2, 3]


def test_concat_blank_first() -> None:
    """Tests the function with a blank list first."""
    a_list: list[int] = list()
    b_list: list[int] = [4, 5, 6]
    assert concat(a_list, b_list) == [4, 5, 6]


def test_concat_blank_second() -> None:
    """Tests the function normally."""
    a_list: list[int] = [1, 2, 3]
    b_list: list[int] = [7, 8, 9]
    assert concat(a_list, b_list) == [1, 2, 3, 7, 8, 9]


def test_concat_blank_both() -> None:
    """Tests the function with two blank lists."""
    a_list: list[int] = list()
    b_list: list[int] = list()
    assert concat(a_list, b_list) == []
