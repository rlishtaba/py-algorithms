from py_algorithms.challenges.various.quarantine.dp import CountTransformations


class TestCountTransformations:
    def test_algorithm(self):
        f = CountTransformations()
        assert f(a="abcccdf", b="abccdf") == 3
        assert f(a="aabba", b="ab") == 4
