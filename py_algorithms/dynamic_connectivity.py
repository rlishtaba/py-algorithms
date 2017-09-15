import abc
from typing import List


def dynamic_connectivity_brute_force(components: List[int]) -> 'DynamicConnectivity':
    return _BruteForce(components)


def dynamic_connectivity_quick_union(components: List[int]) -> 'DynamicConnectivity':
    return _QuickUnion(components)


class DynamicConnectivity(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def is_connected(self, a: int, b: int) -> bool:
        pass

    @abc.abstractmethod
    def connect(self, a: int, b: int) -> None:
        pass


class _BruteForce(DynamicConnectivity):
    def __init__(self, components: List[int]):
        self._components = components

    def is_connected(self, a: int, b: int) -> bool:
        return self._components[a] == self._components[b]

    def connect(self, a: int, b: int) -> None:
        a_ptr = self._components[a]
        b_ptr = self._components[b]
        # test if already connected
        if a_ptr == b_ptr:
            return

        for i, x in enumerate(self._components):
            if self._components[i] == a_ptr:
                self._components[i] = b_ptr


class _QuickUnion(DynamicConnectivity):
    def __init__(self, components: List[int]):
        self._components = components

    def is_connected(self, a: int, b: int) -> bool:
        return self._root(a) == self._root(b)

    def connect(self, a: int, b: int) -> None:
        a_ptr = self._root(a)
        b_ptr = self._root(b)
        self._components[a_ptr] = b_ptr

    def _root(self, x: int) -> int:
        while x != self._components[x]:
            x = self._components[x]
        return x
