from typing import Any
from typing import List

__all__ = [
    'new_powerset'
]

from .powerset import PowerSet


def new_powerset(xs: List[Any]) -> List[Any]:
    """
    Factory method
    :param xs: List
    :return: List of Lists
    """
    return PowerSet.apply(xs)
