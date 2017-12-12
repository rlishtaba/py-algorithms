import pytest

from py_algorithms.array.longest_consecutive import LongestConsecutive


def _test_case_helper(f, mapping):
    for x in mapping:
        payload, expected = x
        assert expected == f(payload)


@pytest.fixture
def cases():
    return [
        ([100, 4, 200, 1, 3, 2], 4),
        ([], 0),
        ([2, 1, 1, 3], 3)]


class TestLongestConsecutive:
    def test_apply(self):
        _test_case_helper(LongestConsecutive.with_sorting, cases())

    def test_brute_force(self):
        _test_case_helper(LongestConsecutive.brute_force, cases())

    def test_with_set(self):
        _test_case_helper(LongestConsecutive.with_set, cases())
