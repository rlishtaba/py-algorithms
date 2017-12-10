from py_algorithms.array import new_circular_array


class TestCircularArray:
    def test_circular_array(self):
        arr = new_circular_array(5)

        for i in range(0, 10):
            arr.enqueue(i)

        assert arr.size() == 10

        for _ in range(9, -1, -1):
            arr.dequeue()

        assert arr.size() == 0
