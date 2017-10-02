import math
from typing import List

from ..utils import test_iterable
from ..utils import three_way_cmp
from .sort import Sort


class CombSort(Sort):
    _SHRINK = 1.3
    """
    Worst-case: О(n^2)
    Best-case: O(n log n)
    Space: О(1)
    Stability: true
    """

    def sort(self, xs: List[int]) -> List[int]:
        test_iterable(xs)

        gap = len(xs)
        in_order = False

        while not in_order:
            gap = math.floor(gap / self._SHRINK)  # simply gap * 10 // 13

            if gap < 1:
                gap = 1

            swapped = False
            for i in range(len(xs) - gap):
                if three_way_cmp(xs[i], xs[i + gap]) == 1:
                    xs[i], xs[i + gap] = xs[i + gap], xs[i]
                    swapped = True
            if not swapped and gap == 1:
                in_order = True

        return xs
