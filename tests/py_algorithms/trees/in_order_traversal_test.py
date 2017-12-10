from py_algorithms.trees import in_order_traversal
from py_algorithms.trees import new_bst_from_list


class TestLevelOrderTraversal:
    def test_apply(self):
        exponent = 7
        xs = list(range((2 ** exponent) - 1))
        root = new_bst_from_list(xs)
        ordered = in_order_traversal(root)

        assert ordered == xs
