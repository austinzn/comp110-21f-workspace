"""List utility functions."""

__author__ = "730466197"


def all(integers: list[int], search: int) -> bool:
    """Tells you if a list of intergers is all the same number or not."""
    i: int = 0
    x: int = 0
    if len(integers) > 0:
        while i < len(integers):
            if integers[i] == search:
                x += 1
            i += 1
        if x == len(integers):
            return True
        else:
            return False
    else:
        return False


def is_equal(integers_one: list[int], integers_two: list[int]) -> bool:
    """Tells you if two lists are deeply equal."""
    if len(integers_one) == len(integers_two):
        i: int = 0
        x: int = 0
        while i < len(integers_one):
            if integers_one[i] == integers_two[i]:
                x += 1
            i += 1
        if x == len(integers_one):
            return True
    return False


def max(integers: list[int]) -> int:
    """Finds the largest number in a list."""
    i: int = 0
    x: int = integers[0]
    while i < len(integers):
        if integers[i] > x:
            x = integers[i]
        i += 1
    return x