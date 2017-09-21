from py_algorithms.data_structures import new_priority_queue


class TestQueue:
    def test_properties(self):
        pq = new_priority_queue(lambda x, y: (x > y) - (x < y) == 1)
        assert pq.is_empty is True
        assert pq.size == 0

    def test_push_and_pop(self):
        pq = new_priority_queue(lambda x, y: (x > y) - (x < y) == -1)
        pq.push('one', 1)
        pq.push('two', 2)
        assert pq.is_empty is False
        assert pq.size == 2
        assert pq.next == 'one'
        assert pq.pop() == 'one'
        assert pq.has_priority(1) is True
        assert pq.clear()
        assert pq.has_priority(1) is False

    def test_corner_cases(self):
        pq = new_priority_queue(lambda x, y: (x > y) - (x < y) == -1)
        assert pq.is_empty is True
        assert pq.size == 0
        assert pq.pop() is None
