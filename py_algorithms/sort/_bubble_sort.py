from typing import List

from ..utils import test_iterable
from ..utils import three_way_cmp
from .sort import Sort


class BubbleSort(Sort):
    """
        Simple sorting algorithm

        Stability: yes
        N: len(XS)
        Time: O(N^2)
        Space: O(N)
    """

    def sort(self, xs: List[int]) -> List[int]:
        test_iterable(xs)

        done = False
        while not done:
            swapped = False
            for i in range(0, len(xs) - 1):
                # compare current item with next one,
                # if current bigger than next one - swap it, mark state flag
                if 1 == three_way_cmp(xs[i], xs[i + 1]):
                    xs[i], xs[i + 1] = xs[i + 1], xs[i]
                    swapped = True
            # all items are in order now
            if not swapped:
                done = True
        return xs
