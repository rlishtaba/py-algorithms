from typing import Callable
from typing import List

from ._bubble_sort import BubbleSort
from .sort import Sort

__all__ = [
    'new_bubble_sort',
    'Sort'
]


def new_bubble_sort() -> Callable[[List[int]], List[int]]:
    """
    Factory method to return function to sort
    :return: a function1 interface to apply
    """
    return lambda xs: BubbleSort().sort(xs)
