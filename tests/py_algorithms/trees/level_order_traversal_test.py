from py_algorithms.trees import level_order_traversal
from py_algorithms.trees import new_bst_from_list


class TestLevelOrderTraversal:
    def test_apply(self):
        xs = list(range((2 ** 6) - 1))
        root = new_bst_from_list(xs)
        levels = level_order_traversal(root)

        for i, level in enumerate(levels):
            assert len(level) == 2 ** i
