"""Practice with dictionaries."""

__author__ = "730466197"


def invert(pair: dict[str, str]) -> dict[str, str]:
    new_list: dict[str, str]
    new_list = dict()
    for key in pair:
        new_list[pair[key]] = key
    return new_list