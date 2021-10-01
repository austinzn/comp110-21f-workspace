"""List utility functions part 2."""

__author__ = "730466197"

# Define your functions below
def only_evens(xs: list[int]) -> list[int]:
    """Returns only the even numbers of a list of numbers."""
    i: int = 0
    count: list[int] = list()
    while i < len(xs):
        if xs[i] % 2 == 0:
            count.append(xs[i])
        i += 1
    return count


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Generates a subset of the given list within the set parameters."""
    i: int = 0
    subset: list[int] = list()
    while i < len(xs):
        if start <= i < end:
            subset.append(xs[i])
        i += 1
    return subset


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Generates a list comprised of the first list followed by the second."""
    i: int = 0
    new: list[int] = xs
    while i < len(ys):
        new.append(ys[i])
        i += 1
    return new
