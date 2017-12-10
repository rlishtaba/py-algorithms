from py_algorithms.trees import find_range_in_bst
from py_algorithms.trees import new_bst_from_list


class TestFindRangeInBst:
    def test_apply(self):
        exponent = 7
        xs = list(range((2 ** exponent) - 1))
        bst = new_bst_from_list(xs)
        r = find_range_in_bst(bst, 10, 47)
        assert r == list(range(10, 47 + 1))
