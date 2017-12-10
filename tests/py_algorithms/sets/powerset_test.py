from py_algorithms.sets import new_powerset


class TestPowerSet:
    def test_powerset(self):
        powerset = new_powerset([1, 2, 3])
        assert len(powerset) == 2 ** 3
        assert powerset == [[], [1], [2], [1, 2],
                            [3], [1, 3], [2, 3], [1, 2, 3]]

    def test_two_elements_powerset(self):
        powerset = new_powerset([1, 2])
        assert len(powerset) == 2 ** 2
        assert powerset == [[], [1], [2], [1, 2]]

    def test_single_element_powerset(self):
        powerset = new_powerset([1])
        assert len(powerset) == 2 ** 1
        assert powerset == [[], [1]]

    def test_empty_powerset(self):
        powerset = new_powerset([])
        assert len(powerset) == 2 ** 0
        assert powerset == [[]]

    def test_chars_powerset(self):
        powerset = new_powerset(list("abc"))
        expected = ['', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc']
        assert len(powerset) == 2 ** 3
        assert [''.join(x) for x in powerset] == expected

    def test_large_powerset(self):
        s = [x for x in range(1 << 4)]
        powerset = new_powerset(s)
        assert len(powerset) == 1 << len(s)
