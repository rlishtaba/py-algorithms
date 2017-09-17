import copy
from typing import List

import pytest

from py_algorithms.data_structures import new_deque


@pytest.fixture
def collection() -> List[int]:
    return [0, 6, 7, 8, 9, 4, 5, 12]


class TestDeque:
    def test_properties(self):
        items = collection()
        deque = new_deque(copy.deepcopy(items))
        assert deque.is_empty() is False
        assert deque.size == len(items)
        assert deque.clear() == 0
        assert deque.is_empty() is True
        assert deque.size == 0

    def test_push_front(self):
        deque = new_deque()
        deque.push_front(1)
        assert deque.front == 1
        assert deque.back == 1
        deque.push_front(2)
        assert deque.front == 2
        assert deque.back == 1

    def test_push_back(self):
        deque = new_deque()
        deque.push_back(1)
        assert deque.front == 1
        assert deque.back == 1
        deque.push_back(2)
        assert deque.front == 1
        assert deque.back == 2
        deque.push_back(3)
        assert deque.front == 1
        assert deque.back == 3

    def test_pop_front_with_one_item(self):
        deque = new_deque()
        deque.push_front(1)
        assert deque.front == 1
        assert deque.back == 1
        val = deque.pop_front()
        assert val == 1
        assert deque.clear() == 0
        assert deque.is_empty() is True
        assert deque.size == 0

    def test_pop_front(self):
        deque = new_deque()
        items = [1, 3, 2, 7]
        expected = []
        for x in items:
            # preserve order for a test
            deque.push_back(x)

        for _ in range(0, len(items)):
            expected.append(deque.pop_front())

        assert items == expected

    def test_pop_back(self):
        deque = new_deque()
        items = [1, 3, 2, 7]
        expected = []
        for x in items:
            # preserve order for a test
            deque.push_front(x)

        for _ in range(0, len(items)):
            expected.append(deque.pop_back())

        assert items == expected
