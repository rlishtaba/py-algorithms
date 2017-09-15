import abc
from typing import List


def dynamic_connectivity_brute_force(components: List[int]) -> 'DynamicConnectivity':
    return _BruteForce(components)


class DynamicConnectivity(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def is_connected(self, a: int, b: int) -> bool:
        pass

    @abc.abstractmethod
    def connect(self, a: int, b: int) -> bool:
        pass


class _BruteForce(DynamicConnectivity):
    def __init__(self, components: List[int]):
        self._components = components

    def is_connected(self, a: int, b: int) -> bool:
        return self._components[a] == self._components[b]

    def connect(self, a: int, b: int) -> bool:
        a_ptr = self._components[a]
        b_ptr = self._components[b]
        # test if already connected
        if a_ptr == b_ptr:
            return True

        for i, x in enumerate(self._components):
            if self._components[i] == a_ptr:
                self._components[i] = b_ptr
