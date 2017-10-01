from ._binary_search import _BinarySearch
from .search import Search

__all__ = ['Search', 'new_binary_search']


def new_binary_search() -> Search:
    """
    Generic, classic Binary Search implementation

        >>> from py_algorithms.search import new_binary_search
        >>>
        >>> algorithm = new_binary_search() # type: Search
        >>> algorithm.search([0, 4, 5, 6, 7, 8, 9, 12], 12) #=> 12

    :return: None or target
    """
    return _BinarySearch()
