import pytest

from py_algorithms.primality_tests import new_simple_primality_test
from tests.conftest import primes_0_3000, big_primes


@pytest.fixture
def algorithm():
    return new_simple_primality_test()


class TestSimplePrimalityTest:
    def test_simple_primality_test(self):
        algo = algorithm()
        for prime in primes_0_3000():
            assert algo(prime) is True

    def test_simple_primality_test_on_non_primes(self):
        algo = algorithm()
        for non_prime in map(lambda x: x + 1, primes_0_3000()[1:]):
            assert algo(non_prime) is False

    def test_against_big_primes(self):
        algo = algorithm()
        for prime in big_primes():
            assert algo(prime) is True
