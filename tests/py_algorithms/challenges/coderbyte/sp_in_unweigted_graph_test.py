from py_algorithms.challenges.coderbyte.sp_in_unweigted_graph import SPUnweightedCyclicGraph


class TestBinarySearchTreeLca:
    def test_impl(self):
        inputs = {
            'A-B-D': ["4", "A", "B", "C", "D", "A-B", "B-D", "B-C", "C-D"],
            'A-E-D-F-G': ["7", "A", "B", "C", "D", "E", "F", "G", "A-B",
                          "A-E", "B-C", "C-D", "D-F", "E-D", "F-G"],
            'c-s-h-d-m': ["5", "c", "h", "d", "s", "m", "c-s", "s-h", "d-m", "h-d"],
            'N1-N2-N5': ["5", "N1", "N2", "N3", "N4", "N5", "N1-N3",
                         "N3-N4", "N4-N5", "N5-N2", "N2-N1"]
        }

        f = SPUnweightedCyclicGraph()
        for key in inputs:
            assert f(inputs[key]) == key
