"""
This module is part of the 'sitzungsdienst' package,
which is released under GPL-3.0-only license.
"""

from hashlib import blake2b
from typing import Any, Iterable


def data2hash(data: Any) -> str:
    """
    Builds hash over given data

    :param data: typing.Any Data
    :return: str Hash
    """

    return blake2b(str(data).encode("utf-8"), usedforsecurity=False).hexdigest()


def flatten(data: Iterable[Iterable[Any]]) -> list[Any]:
    """
    Flattens list of lists

    :param data: typing.Iterable[typing.Iterable[typing.Any]] List of lists
    :return: list Flattened list
    """

    return [item for sublist in data for item in sublist]


def sort_din5007(string: str) -> tuple[str, str]:
    """
    Sorts strings with german umlauts according to DIN 5007 ('sorted' helper)

    :param string: str Input string
    :return: tuple Strings for comparison
    """

    # Lowercase string
    lowercase = string.lower()

    # Replace umlauts
    lowercase = lowercase.replace("ä", "a")
    lowercase = lowercase.replace("ö", "o")
    lowercase = lowercase.replace("ü", "u")
    lowercase = lowercase.replace("ß", "ss")

    return (lowercase, string.swapcase())
