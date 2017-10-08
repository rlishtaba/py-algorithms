from py_algorithms.challenges.coderbyte.subset_sum import SubsetSum


class TestSubsetSum:
    def test_impl(self):
        f = SubsetSum()
        assert f([1, 2, 3], 5) == [[2, 3]]
        assert f([1, 2, 3, 4], 5) == [[2, 3], [1, 4]]
        assert f([1, 2, 3, 4], 7) == [[3, 4], [1, 2, 4]]
