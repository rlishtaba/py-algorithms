from typing import List

from ..utils import test_iterable
from .sort import Sort


class QuickSort(Sort):
    """
    Worst-case: О(n^2)
    Best-case: O(n log n)
    Average: O(n log n)
    Space: О(n) naive
    Stability: no
    """

    def sort(self, xs: List[int]) -> List[int]:
        test_iterable(xs)

        top = {0: 0}
        bottom = {0: len(xs)}
        i = 0

        while i >= 0:
            l = top[i]
            r = bottom[i] - 1
            if l < r:
                pivot = xs[l]
                while l < r:
                    while xs[r] >= pivot and l < r:
                        r -= 1
                    if l < r:
                        xs[l] = xs[r]
                        l += 1
                    while xs[l] <= pivot and l < r:
                        l += 1
                    if l < r:
                        xs[r] = xs[l]
                        r -= 1
                xs[l] = pivot
                top[i + 1] = l + 1
                bottom[i + 1] = bottom[i]
                bottom[i] = l
                i += 1
            else:
                i -= 1

        return xs
