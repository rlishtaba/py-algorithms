import pytest

from py_algorithms.challenges.challenges import Challenges


@pytest.fixture
def mod():
    return Challenges


class TestChallenges:
    def test_first_factorial(self):
        assert mod().first_factorial(0) == 1
        assert mod().first_factorial(1) == 1
        assert mod().first_factorial(8) == 40320
        assert mod().first_factorial(8) == 40320

    def test_longest_word(self):
        assert mod().longest_word("The quick brown fox jumped over the lazy dog") == 'jumped'
        assert mod().longest_word(
            "a confusing /:sentence:/[ wow!!!+!!~") == 'confusing'

    def test_letter_mutation(self):
        assert mod().letter_mutation("hello") == "Ifmmp"
        assert mod().letter_mutation("helloz") == "IfmmpA"
        vowels = ''.join([chr(z) for z in [ord(i) - 1 for i in list("aeiou")]])
        assert mod().letter_mutation(vowels) == "`EIOU"
