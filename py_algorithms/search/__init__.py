from ._binary_search import _BinarySearch
from .search import Search

__all__ = ['Search', 'binary_search']


def binary_search() -> Search:
    return _BinarySearch()
