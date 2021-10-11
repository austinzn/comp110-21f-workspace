"""Practice with dictionaries."""

__author__ = "730466197"


def invert(pair: dict[str, str]) -> dict[str, str]:
    """Inverts the key and value in a dictionary."""
    new_list: dict[str, str]
    new_list = dict()
    for key in pair:
        if pair[key] in new_list:
            raise KeyError
        else:
            new_list[pair[key]] = key
    return new_list


def favorite_color(favorite: dict[str, str]) -> str:
    """Returns the most favorite color in a dictionary of favorite colors."""
    colors: dict[str, int] = dict()
    for key in favorite:
        if favorite[key] in colors:
            colors[favorite[key]] += 1
        else:
            colors[favorite[key]] = 1
    most_favorited: str = ""
    max: int = 0
    for key in colors:
        if colors[key] > max:
            max = colors[key]
            most_favorited = key
    return most_favorited


def count(xs: list[str]) -> dict[str, int]:
    """Returns the most input value."""
    numbers: dict[str, int] = dict()
    i: int = 0
    while i < len(xs):
        if xs[i] in numbers:
            numbers[xs[i]] += 1
        else:
            numbers[xs[i]] = 1
        i += 1
    return numbers