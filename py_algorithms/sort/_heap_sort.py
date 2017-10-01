from typing import List

from ..data_structures import new_min_heap
from ..utils import test_iterable
from .sort import Sort


class FibonacciHeapSort(Sort):
    """
    - Fibonacci Heap Sort. Factory method to return sort functor.

        >>> from py_algorithms.sort import new_heap_sort
        >>>
        >>> xs = [0, 6, 7, 8, 9, 4, 5, 12, -1]
        >>> sorting_algorithm = new_heap_sort()
        >>> sorting_algorithm(xs) #=> [-1, 0, 4, 5, 6, 7, 8, 9, 12]

    Worst case: О(n log n)
    Best case: О(n)
    Average: О(n log n)
    Worst case space: O(1)
    """

    def sort(self, xs: List[int]) -> List[int]:
        test_iterable(xs)

        heap = new_min_heap(xs)
        xs = []
        while not heap.is_empty:
            xs.append(heap.pop())
        return xs


class HeapSort(FibonacciHeapSort):
    pass
