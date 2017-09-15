from typing import List

import pytest

from py_algorithms.search import binary_search
from py_algorithms.search import Search


@pytest.fixture
def collection() -> List[int]:
    return [0, 6, 7, 8, 9, 4, 5, 12]


def helper(algo: Search) -> None:
    assert algo.search(collection(), 0) == 0
    assert algo.search(collection(), 8) == 8
    assert algo.search(collection(), 12) == 12
    assert algo.search(collection(), 9999) is None


class TestCommonSearchAlgorithms:
    def testBinarySearch(self):
        helper(binary_search())
