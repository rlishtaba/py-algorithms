from typing import List

from ..utils import test_iterable
from ..utils import three_way_cmp
from .sort import Sort


class SelectionSort(Sort):
    """
    Time: О(n^2)
    Space: О(n)
    Stability: true
    """

    def sort(self, xs: List[int]) -> List[int]:
        test_iterable(xs)

        for i in range(0, len(xs)):
            min_val = i
            for j in range(i + 1, len(xs)):
                if three_way_cmp(xs[j], xs[min_val]) == -1:
                    min_val = j
            xs[i], xs[min_val] = xs[min_val], xs[i]
        return xs
