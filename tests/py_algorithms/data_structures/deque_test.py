import copy
from typing import List

import pytest

from py_algorithms.data_structures import new_deque


@pytest.fixture
def collection() -> List[int]:
    return [0, 6, 7, 8, 9, 4, 5, 12]


class TestDeque:
    def testProperties(self):
        items = collection()
        deque = new_deque(copy.deepcopy(items))
        assert deque.is_empty() is False
        assert deque.size == len(items)
        assert deque.clear() == 0
        assert deque.is_empty() is True
        assert deque.size == 0

    def testPushFront(self):
        deque = new_deque()
        deque.push_front(1)
        assert deque.front == 1
        assert deque.back == 1
        deque.push_front(2)
        assert deque.front == 1
        assert deque.back == 2

    def testPushBack(self):
        deque = new_deque()
        deque.push_back(1)
        assert deque.front == 1
        assert deque.back == 1
        deque.push_back(2)
        assert deque.front == 2
        assert deque.back == 1
        deque.push_back(3)
        assert deque.front == 3
        assert deque.back == 1

    def testPopFrontWithOneItem(self):
        deque = new_deque()
        deque.push_front(1)
        assert deque.front == 1
        assert deque.back == 1
        val = deque.pop_front()
        assert val == 1
        assert deque.clear() == 0
        assert deque.is_empty() is True
        assert deque.size == 0

    def testPopFront(self):
        deque = new_deque()
        items = [1, 3, 2, 7]
        expected = []
        for x in items:
            # preserve order for a test
            deque.push_back(x)

        for _ in range(0, len(items)):
            expected.append(deque.pop_front())

        assert items == expected

    def testPopBack(self):
        deque = new_deque()
        items = [1, 3, 2, 7]
        expected = []
        for x in items:
            # preserve order for a test
            deque.push_front(x)

        for _ in range(0, len(items)):
            expected.append(deque.pop_back())

        assert items == expected
