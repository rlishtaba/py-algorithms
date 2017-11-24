import pytest

from py_algorithms.primality_tests import new_miller_rabin_primality_test
from tests.conftest import primes_0_3000, big_primes


@pytest.fixture
def algorithm():
    return new_miller_rabin_primality_test()


class TestMillerRabin:
    def test_miller_rabin_primality_test(self):
        algo = algorithm()
        for prime in primes_0_3000():
            assert algo(prime) is True

    def test_miller_rabin_primality_test_on_non_primes(self):
        def test_bed(xs, f):
            for non_prime in xs:
                assert f(non_prime) is False

        non_primes = list(map(lambda x: x + 1, primes_0_3000()))
        test_bed(non_primes[1:], algorithm())

    def test_against_big_primes(self):
        algo = algorithm()
        for prime in big_primes():
            assert algo(prime) is True
