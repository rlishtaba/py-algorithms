from py_algorithms.challenges.coderbyte.weighted_path import WeightedPath


class TestWeightedPath:
    def test_impl(self):
        inputs = {
            "A-B-C-D-F-G": ["7", "A", "B", "C", "D", "E", "F", "G",
                            "A|B|1", "A|E|9", "B|C|2", "C|D|1", "D|F|2",
                            "E|D|6", "F|G|2"],
            "A-B-C-D": ["4", "A", "B", "C", "D", "A|B|1", "B|D|9", "B|C|3",
                        "C|D|4"],
            -1: ["4", "x", "y", "z", "w", "x|y|2", "y|z|14", "z|y|31"],
            "A-B-D": ["4", "A", "B", "C", "D", "A|B|2", "C|B|11", "C|D|3",
                      "B|D|2"],
            "A-B-D-E-F": ["6", "A", "B", "C", "D", "E", "F", "B|A|2",
                          "A|F|12", "A|C|4", "B|D|1", "D|E|1", "C|D|4",
                          "F|E|1"],
            "D-B-A-F": ["6", "D", "B", "C", "A", "E", "F", "B|A|2",
                        "A|F|3", "A|C|4", "B|D|1", "D|E|12", "C|D|4",
                        "F|E|1"],
            "C-D-F-G-E-B-H": ["8", "C", "B", "A", "D", "E", "F", "G",
                              "H", "C|D|1", "D|F|2", "G|F|2", "G|E|1", "E|B|1",
                              "H|B|1", "C|A|13", "B|A|2", "C|E|9"],
            "GG-HH-JJ": ["3", "GG", "HH", "JJ", "GG|JJ|6", "GG|HH|2", "JJ|HH|2"],
            "C-E-B-H": ["8", "C", "B", "A", "D", "E", "F", "G", "H", "C|D|1",
                        "D|F|2", "G|F|2", "G|E|1", "E|B|1", "H|B|1",
                        "C|A|13", "B|A|2", "C|E|1"]
        }

        f = WeightedPath()
        for key in inputs:
            assert f(inputs[key]) == key
