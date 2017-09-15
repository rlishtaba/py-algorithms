import abc
import copy
from typing import List


def dynamic_connectivity_brute_force(xs: List[int]) -> 'DynamicConnectivity':
    return _BruteForce(xs)


def dynamic_connectivity_quick_union(xs: List[int]) -> 'DynamicConnectivity':
    return _QuickUnion(xs)


def dynamic_connectivity_weighted_quick_union(xs: List[int]) -> 'DynamicConnectivity':
    return _WeighedQuickUnion(xs)


def dynamic_connectivity_weighted_quick_union_pc(xs: List[int]) -> 'DynamicConnectivity':
    return _WeightedQuickUnionPC(xs)


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


class _WeighedQuickUnion(_QuickUnion):
    """
        N = len(components)
        Runtime N * Log N
    """

    def __init__(self, components: List[int]):
        super().__init__(components)
        self._tree_size = copy.deepcopy(components)

    def connect(self, a: int, b: int) -> None:
        a_ptr = self._root(a)
        b_ptr = self._root(b)

        # test if already connected
        if a_ptr == b_ptr:
            return

        # attach smaller tree to bigger one
        if self._tree_size[a_ptr] < self._tree_size[b_ptr]:
            self._components[a_ptr] = b_ptr
            self._tree_size[b_ptr] += self._tree_size[a_ptr]
        else:
            self._components[b_ptr] = a_ptr
            self._tree_size[a_ptr] += self._tree_size[b_ptr]


class _WeightedQuickUnionPC(_WeighedQuickUnion):
    def _root(self, x: int) -> int:
        root = x
        while root != self._components[root]:
            root = self._components[root]

        while x != root:
            new_root = self._components[x]
            self._components[x] = root
            x = new_root

        return root
