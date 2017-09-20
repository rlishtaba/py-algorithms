import pytest

from py_algorithms.data_structures.heap import Heap


@pytest.fixture
def int_max_heap() -> Heap:
    # max property, for integer based keys
    return Heap(lambda x, y: (x > y) - (x < y) == 1)


class TestHeap:
    def test_properties(self):
        ds = int_max_heap()
        assert ds.size == 0
        assert ds.is_empty is True

    def test_push(self):
        ds = int_max_heap()
        ds.push(1, 11)
        ds.push(2, 12)
        ds.push(3, 13)
        assert ds.is_empty is False
        assert ds.next_key == 3
        assert ds.next_key == 3
        assert ds.contains_key(2) is True
        assert ds.contains_key('the key') is False

    def test_pop(self):
        ds = int_max_heap()
        ds.push(1, 11)
        ds.push(2, 12)
        ds.push(3, 13)
        assert ds.pop() == 13
        assert ds.pop() == 12
        assert ds.push(-1, 10)
        assert ds.next == 11
        assert ds.push(100, 99)
        assert ds.next == 99
        assert ds.contains_key(100) is True
        assert ds.contains_key(101) is False
