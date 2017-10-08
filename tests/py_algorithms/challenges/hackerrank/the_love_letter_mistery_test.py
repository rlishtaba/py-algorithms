from py_algorithms.challenges.hackerrank.the_love_letter_mistery import LoveLetterMystery


class TestLoveLetterMystery:
    _VOWELS = ''.join([chr(z) for z in [ord(i) - 1 for i in list("aeiou")]])

    def test_impl(self):
        f = LoveLetterMystery()
        assert f('abc') == 2
        assert f('abcba') == 0
        assert f('abcd') == 4
        assert f('cba') == 2
