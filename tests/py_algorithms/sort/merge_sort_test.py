import random
from typing import List

import pytest

from py_algorithms.sort import new_merge_sort


@pytest.fixture
def xs() -> List[int]:
    return [0, 6, 7, 8, 9, 4, 5, 12, -1]


def large_xs() -> List[int]:
    raw = [0, 6, 7, 8, 9, 4, 5, 12, -112] * 50
    random.shuffle(raw)
    return raw


class TestMergeSort:
    def test_sorting_algorithm(self):
        f = new_merge_sort()
        assert sorted(xs()) == f(xs())

    def test_sorting_algorithm_on_large_xs(self):
        f = new_merge_sort()
        assert sorted(large_xs()) == f(large_xs())

    def test_non_iterable_xs(self):
        f = new_merge_sort()
        for x in (None, 1, ''):
            with pytest.raises(RuntimeError):
                f(x)
