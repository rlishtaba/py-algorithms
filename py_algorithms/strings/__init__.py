__all__ = [
    'new_boyer_moore_find'
]

from typing import Callable, List, Any
from .boyer_moore_find import BoyerMooreFind
from .levenshtein_distance import LevenshteinDistance


def new_boyer_moore_find() -> Callable[[str, str], int]:
    return BoyerMooreFind()


def new_levenshtein_distance(a: List[Any], b: List[Any]) -> int:
    """
    Factory Method
    :param a: List
    :param b: List
    :return: int
    """
    return LevenshteinDistance.apply(a, b)
