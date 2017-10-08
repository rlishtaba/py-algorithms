from py_algorithms.challenges.coderbyte.power_set import PowerSet


class TestPowerSet:
    def test_impl(self):
        expected = [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
        f = PowerSet()
        assert f([1, 2, 3]) == expected
