from py_algorithms.challenges.coderbyte.binary_search_tree_lca import BinarySearchTreeLca


class TestBinarySearchTreeLca:
    def test_impl(self):
        inputs = {
            5: ["[10, 5, 1, 7, 40, 50]", "1", "7"],
            12: ["[3, 2, 1, 12, 4, 5, 13]", "5", "13"],
            10: ["[10, 5, 1, 7, 40, 50]", "5", "10"],
        }
        f = BinarySearchTreeLca()
        for key in inputs:
            assert f(inputs[key]) == key
