from typing import List

from ..utils import test_iterable
from .sort import Sort


class RecursiveMergeSort(Sort):
    """
    Time: О(N log N)
    Space: О(N)
    Stability: true

    Recursive implementation
    """

    def sort(self, xs: List[int]) -> List[int]:
        test_iterable(xs)
        if len(xs) <= 1:
            return xs

        mid = len(xs) // 2
        left = xs[:mid]
        right = xs[mid:]

        return self.merge(self.sort(left), self.sort(right))

    @staticmethod
    def merge(left: List[int], right: List[int]) -> List[int]:
        xs = []
        while not (len(left) == 0 or len(right) == 0):
            if left[0] <= right[0]:
                xs.append(left.pop(0))
            else:
                xs.append(right.pop(0))
        return xs + left + right
