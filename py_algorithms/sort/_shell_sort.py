from typing import List

from ..utils import test_iterable
from .sort import Sort


class ShellSort(Sort):
    """
    Worst-case: О(n ^ 2)
    Best-case: O(n log n)
    Space: О(n)
    Stability: true
    """

    def sort(self, xs: List[int]) -> List[int]:
        test_iterable(xs)

        inc = len(xs) // 2
        while inc > 0:
            for i in range(inc, len(xs)):
                temp = xs[i]
                j = i
                while j >= inc and xs[j - inc] > temp:
                    xs[j] = xs[j - inc]
                    j -= inc
                xs[j] = temp
            if inc == 2:
                inc = 1
            else:
                inc = int(round(inc // 2.2, 0))
        return xs
