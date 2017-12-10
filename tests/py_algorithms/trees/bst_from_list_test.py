from math import ceil
from math import log2

from py_algorithms.trees.bst_from_list import BstFromList


def tree_height(root):
    if root is None:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))


class TestBstFromList:
    def test_apply(self):
        exponent = 7
        xs = list(range((2 ** exponent) - 1))
        tree = BstFromList.apply(xs)
        height = tree_height(tree)
        assert height == exponent
        assert height == ceil(log2(len(xs)))
