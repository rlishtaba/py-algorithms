from typing import Callable
from typing import List

import pytest

from py_algorithms.sort import new_comb_sort
from tests.conftest import large_xs
from tests.conftest import xs


@pytest.fixture
def new_sorting_algorithm() -> Callable[[List[int]], List[int]]:
    return new_comb_sort()


class TestCombSort:
    def test_sorting_algorithm(self):
        f = new_sorting_algorithm()
        assert sorted(xs()) == f(xs())

    def test_sorting_algorithm_on_large_xs(self):
        f = new_sorting_algorithm()
        assert sorted(large_xs()) == f(large_xs())

    def test_non_iterable_xs(self):
        f = new_sorting_algorithm()
        for x in (None, 1, ''):
            with pytest.raises(RuntimeError):
                f(x)
