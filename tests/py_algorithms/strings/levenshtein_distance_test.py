from py_algorithms.strings import new_levenshtein_distance


class TestLevenshteinDistance:
    def test_apply(self):
        a = "Orchestra"
        b = "Carthorse"
        dst = new_levenshtein_distance(list(a), list(b))
        assert dst == 8

    def test_apply_dst_1(self):
        dst = new_levenshtein_distance(list('Moon'), list("Moore"))
        assert dst == 2
