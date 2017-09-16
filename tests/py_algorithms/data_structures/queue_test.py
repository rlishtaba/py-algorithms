import copy
from typing import List

import pytest

from py_algorithms.data_structures import new_queue


@pytest.fixture
def collection() -> List[int]:
    return [0, 6, 7, 8, 9, 4, 5, 12]


class TestQueue:
    def testProperties(self):
        items = collection()
        queue = new_queue(copy.deepcopy(items))
        assert queue.is_empty() is False
        assert queue.size == len(items)
        for _ in range(0, len(items) - 1):
            queue.pop()
        assert queue.next() == items[len(items) - 1]
