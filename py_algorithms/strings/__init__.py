__all__ = [
    'new_boyer_moore_find'
]

from typing import Callable
from .boyer_moore_find import BoyerMooreFind


def new_boyer_moore_find() -> Callable[[str, str], int]:
    return BoyerMooreFind()
