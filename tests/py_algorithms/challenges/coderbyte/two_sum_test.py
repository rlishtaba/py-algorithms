from py_algorithms.challenges.coderbyte.two_sum import TwoSum


class TestTwoSum:
    def test_impl(self):
        f = TwoSum()
        assert f([3, 5, 2, -4, 8, 11], 7) == [[2, 5], [11, -4]]
        assert f([3, 5, 2, -4, 8, 11], 2) == []
        assert f([3, 5, 2, -4, 8, 11], 8) == [[5, 3]]
