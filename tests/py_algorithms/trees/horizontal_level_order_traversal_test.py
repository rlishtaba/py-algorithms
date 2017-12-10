from py_algorithms.trees import horizontal_level_order_traversal
from py_algorithms.trees import new_bst_from_list


class TestHorizontalLevelOrderTraversal:
    def test_apply(self):
        xs = list(range((2 ** 4) - 1))
        root = new_bst_from_list(xs)
        levels = horizontal_level_order_traversal(root)

        expected = {
            -3: [0],
            -2: [1],
            -1: [8, 3, 4, 2],
            0: [7, 9, 5],
            1: [11, 12, 10, 6],
            2: [13],
            3: [14]
        }

        assert levels == expected
