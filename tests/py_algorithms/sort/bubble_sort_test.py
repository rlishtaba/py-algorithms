import copy
from typing import List

import pytest

from py_algorithms.sort import new_bubble_sort


@pytest.fixture
def xs() -> List[int]:
    return [0, 6, 7, 8, 9, 4, 5, 12]


@pytest.fixture
def sorted_xs() -> List[int]:
    return sorted(xs())


class TestBubbleSort:
    def test_sorting_algorithm(self):
        f = new_bubble_sort()
        assert sorted_xs() == f(xs())
        decreasing_xs = [999, 10, 9, 8, 7, 6]
        assert sorted(copy.copy(decreasing_xs)) == f(decreasing_xs)

    def test_non_iterable_xs(self):
        f = new_bubble_sort()
        for x in (None, 1, ''):
            with pytest.raises(RuntimeError):
                f(x)
