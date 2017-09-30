import copy
import random
from typing import List

import pytest

from py_algorithms.sort import new_bubble_sort


@pytest.fixture
def xs() -> List[int]:
    return [0, 6, 7, 8, 9, 4, 5, 12, -112]


def large_xs() -> List[int]:
    raw = [0, 6, 7, 8, 9, 4, 5, 12, -112] * 50
    random.shuffle(raw)
    return raw


class TestBubbleSort:
    def test_sorting_algorithm(self):
        f = new_bubble_sort()
        assert sorted(xs()) == f(xs())
        decreasing_xs = [999, 10, 9, 8, 7, 6]
        assert sorted(copy.copy(decreasing_xs)) == f(decreasing_xs)

    def test_sorting_algorithm_on_large_set(self):
        f = new_bubble_sort()
        assert sorted(large_xs()) == f(large_xs())
        decreasing_xs = [999, 10, 9, 8, 7, 6]
        assert sorted(copy.copy(decreasing_xs)) == f(decreasing_xs)

    def test_non_iterable_xs(self):
        f = new_bubble_sort()
        for x in (None, 1, ''):
            with pytest.raises(RuntimeError):
                f(x)
