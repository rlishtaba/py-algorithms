import copy
from typing import List

import pytest

from py_algorithms.data_structures import new_stack


@pytest.fixture
def collection() -> List[int]:
    return [0, 6, 7, 8, 9, 4, 5, 12]


class TestStack:
    def test_properties(self):
        items = collection()
        ds = new_stack(copy.deepcopy(items))
        assert ds.is_empty() is False
        assert ds.size == len(items)

    def test_pop(self):
        items = collection()
        ds = new_stack(copy.deepcopy(items))
        for _ in range(0, len(items) - 1):
            ds.pop()
        assert ds.next == items[0]

    def test_pop_push(self):
        ds = new_stack()
        ds.push(10)
        ds.push(9)
        assert ds.next == 9
        assert ds.pop() == 9

    def test_corner_cases(self):
        ds = new_stack()
        assert ds.pop() is None
        ds.push(1)
        ds.pop()
        assert ds.pop() is None
