from py_algorithms.strings import new_boyer_moore_find


class TestBoyerMooreFind:
    def test_correct_substring(self):
        string = "zasallaerer"
        substring = string[3:8]
        algo = new_boyer_moore_find()
        assert algo(string, substring) == 3

    def test_null_substring(self):
        string = "zasallaerer"
        substring = ""
        algo = new_boyer_moore_find()
        assert algo(string, substring) == 0

    def test_not_found_substring(self):
        string = "zasallaerer"
        substring = "zzz"
        algo = new_boyer_moore_find()
        assert algo(string, substring) == -1
