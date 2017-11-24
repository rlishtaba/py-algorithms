__all__ = [
    'new_miller_rabin_primality_test',
    'new_simple_primality_test'
]

from typing import Callable
from .miller_rabin_primality_test import MillerRabinPrimalityTest
from .simple_primality_test import SimplePrimalityTest


def new_miller_rabin_primality_test() -> Callable[[int, int], bool]:
    return MillerRabinPrimalityTest()


def new_simple_primality_test() -> Callable[[int], bool]:
    return SimplePrimalityTest()
