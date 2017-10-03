from typing import Callable
from typing import List

from ._bubble_sort import BubbleSort
from ._comb_sort import CombSort
from ._heap_sort import FibonacciHeapSort
from ._merge_sort import RecursiveMergeSort
from ._quick_sort import QuickSort
from ._selection_sort import SelectionSort
from ._shell_sort import ShellSort
from .sort import Sort

__all__ = [
    'new_bubble_sort',
    'new_merge_sort',
    'new_selection_sort',
    'new_heap_sort',
    'new_shell_sort',
    'new_comb_sort',
    'new_quick_sort',
    'Sort'
]


def new_bubble_sort() -> Callable[[List[int]], List[int]]:
    """
     - Bubble Sort implementation. Factory method to return sort functor.

         >>> from py_algorithms.sort import new_merge_sort
         >>>
         >>> xs = [0, 6, 7, 8, 9, 4, 5, 12, -112]
         >>> sorting_algorithm = new_bubble_sort()
         >>> sorting_algorithm(xs) #=> [-112, 0, 4, 5, 6, 7, 8, 9, 12]

     :return: a function1 interface to apply
     """
    return lambda xs: BubbleSort().sort(xs)


def new_merge_sort() -> Callable[[List[int]], List[int]]:
    """
    - Merge Sort, recursive implementation. Factory method to return sort functor.

        >>> from py_algorithms.sort import new_merge_sort
        >>>
        >>> xs = [0, 6, 7, 8, 9, 4, 5, 12, -1]
        >>> sorting_algorithm = new_merge_sort()
        >>> sorting_algorithm(xs) #=> [-1, 0, 4, 5, 6, 7, 8, 9, 12]

    :return: a function1 interface to apply
    """
    return lambda xs: RecursiveMergeSort().sort(xs)


def new_selection_sort() -> Callable[[List[int]], List[int]]:
    """
    - Selection Sort implementation. Factory method to return sort functor.

        >>> from py_algorithms.sort import new_selection_sort
        >>>
        >>> xs = [0, 6, 7, 8, 9, 4, 5, 12, -1]
        >>> sorting_algorithm = new_selection_sort()
        >>> sorting_algorithm(xs) #=> [-1, 0, 4, 5, 6, 7, 8, 9, 12]

    :return: a function1 interface to apply
    """
    return lambda xs: SelectionSort().sort(xs)


def new_heap_sort() -> Callable[[List[int]], List[int]]:
    """
    - Fibonacci Heap Sort. Factory method to return sort functor.

        >>> from py_algorithms.sort import new_heap_sort
        >>>
        >>> xs = [0, 6, 7, 8, 9, 4, 5, 12, -1]
        >>> sorting_algorithm = new_heap_sort()
        >>> sorting_algorithm(xs) #=> [-1, 0, 4, 5, 6, 7, 8, 9, 12]

    :return: a function1 interface to apply
    """

    return lambda xs: FibonacciHeapSort().sort(xs)


def new_shell_sort() -> Callable[[List[int]], List[int]]:
    """
    - Shell Sort algorithm. Factory method to return sort functor.

        >>> from py_algorithms.sort import new_shell_sort
        >>>
        >>> xs = [0, 6, 7, 8, 9, 4, 5, 12, -1]
        >>> sorting_algorithm = new_heap_sort()
        >>> sorting_algorithm(xs) #=> [-1, 0, 4, 5, 6, 7, 8, 9, 12]

    :return: a function1 interface to apply
    """

    return lambda xs: ShellSort().sort(xs)


def new_comb_sort() -> Callable[[List[int]], List[int]]:
    """
    - Comb Sort algorithm (Improved on Bubble Sort).
    Factory method to return sort functor.

        >>> from py_algorithms.sort import new_comb_sort
        >>>
        >>> xs = [0, 6, 7, 8, 9, 4, 5, 12, -1]
        >>> sorting_algorithm = new_comb_sort()
        >>> sorting_algorithm(xs) #=> [-1, 0, 4, 5, 6, 7, 8, 9, 12]

    :return: a function1 interface to apply
    """

    return lambda xs: CombSort().sort(xs)


def new_quick_sort() -> Callable[[List[int]], List[int]]:
    """
    - Quick Sort algorithm (Improved on Bubble Sort).
    Factory method to return sort functor.

        >>> from py_algorithms.sort import new_quick_sort
        >>>
        >>> xs = [0, 6, 7, 8, 9, 4, 5, 12, -1]
        >>> sorting_algorithm = new_quick_sort()
        >>> sorting_algorithm(xs) #=> [-1, 0, 4, 5, 6, 7, 8, 9, 12]

    :return: a function1 interface to apply
    """

    return lambda xs: QuickSort().sort(xs)
