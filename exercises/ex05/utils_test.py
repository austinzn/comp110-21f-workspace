"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730466197"


def test_only_evens_regular() -> None:
    a_list: list[int] = [1, 2, 3]
    only_evens(a_list)


def test_only_evens_blank() -> None:
    a_list: list[int] = list()
    only_evens(a_list) 