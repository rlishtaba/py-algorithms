import sys
from typing import Any
from typing import Callable
from typing import List
from typing import Union

from ..utils import test_iterable


class _HeapNode:
    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value
        self.degree = 0
        self.marked = False
        self.right = self
        self.left = self
        self.parent = None
        self.child = None

    def is_marked(self) -> bool:
        return self.marked is True


class Heap:
    MAX_MIN = -sys.maxsize

    def __init__(self, comparator_f2: Callable[[Any, Any], bool], xs: List[Any] = ()):
        test_iterable(xs)
        self._size = 0
        self._comparator_f2 = comparator_f2
        self._next = None
        self._stored = {}
        # default initial values
        for x in xs:
            self.push(x, x)

    @staticmethod
    def _get_by_index(array, index) -> Union[None, Any]:
        try:
            return array[index]
        except IndexError:
            return None

    @classmethod
    def _set_entry_by_index(cls, array, index, value):
        if cls._get_by_index(array, index) == cls.MAX_MIN:
            array[index] = value
            return array
        else:
            array.extend([cls.MAX_MIN] * (index - len(array) + 1))
            return cls._set_entry_by_index(array, index, value)

    @property
    def size(self):
        return self._size

    @property
    def next(self) -> Union[Any, None]:
        if self._next:
            return self._next.value
        return None

    @property
    def next_key(self) -> Union[Any, None]:
        if self._next:
            return self._next.key
        return None

    @property
    def is_empty(self) -> bool:
        return self._next is None

    def clear(self) -> 'Heap':
        self._next = None
        self._size = 0
        self._stored = {}
        return self

    def contains_key(self, key) -> bool:
        if self._stored.get(key, None) and self._stored.get(key):
            return True
        return False

    def push(self, key: Any, value: any) -> Any:
        if key is None:
            raise RuntimeError('Could not process heap keys equal to Null.')

        node = _HeapNode(key, value)

        if self._next:
            node.right = self._next
            node.left = self._next.left
            node.left.right = node
            self._next.left = node

            if self._comparator_f2(key, self._next.key):
                self._next = node
        else:
            self._next = node

        self._size += 1

        w = self._next.right
        while w is not self._next:
            w = w.right

        if not self._stored.get(key, None):
            self._stored[key] = []
        self._stored[key].append(node)

        return value

    def pop(self) -> Any:
        if not self._next:
            return None

        popped = self._next
        if self._size == 1:
            self.clear()
            return popped.value

        # things getting hairy here, we need to merge popped
        # `popped` node's children to the root node
        if self._next.child:
            self._next.child.parent = None
            sibling = self._next.child.right
            while not sibling == self._next.child:
                sibling.parent = None
                sibling = sibling.right

            # Merge children into root.
            # If next is a singular root node,
            # make its child pointer the next node
            if self._next.right == self._next:
                self._next = self._next.child
            else:
                next_left, next_right = self._next.left, self._next.right
                current_child = self._next.child
                self._next.right.left = current_child
                self._next.left.right = current_child.right
                current_child.right.left = next_left
                current_child.right = next_right
                self._next = self._next.right
        else:
            self._next.left.right = self._next.right
            self._next.right.left = self._next.left
            self._next = self._next.right

        self._consolidate()

        if not self._stored.get(popped.key, None):
            raise RuntimeError("Could not delete a heap entry.")

        self._size -= 1
        return popped.value

    def _consolidate(self):
        roots = []
        root = self._next
        _min = root

        while True:  # find the nodes in the list
            roots.append(root)
            root = root.right
            if root == self._next:
                break

        degrees = []
        for root in roots:
            if self._comparator_f2(root.key, _min.key):
                _min = root

            # check if we need to merge
            if not self._get_by_index(degrees, root.degree):
                self._set_entry_by_index(degrees, root.degree, root)
            else:
                # there is another node(s) with the same degree,
                # we'll try to consolidate them
                degree = root.degree

                while not (self._get_by_index(degrees, degree) in [self.MAX_MIN, None]):
                    other_root_with_degree = degrees[degree]

                    if self._comparator_f2(root.key, other_root_with_degree.key):
                        # determine which node is the parent, which one is the
                        # child
                        smaller, larger = root, other_root_with_degree
                    else:
                        smaller, larger = other_root_with_degree, root

                    self._link_nodes(larger, smaller)
                    degrees[degree] = self.MAX_MIN
                    root = smaller
                    degree += 1

                self._set_entry_by_index(degrees, degree, root)
                # make sure duplicate keys in the right order
                if _min.key == root.key:
                    _min = root

        self._next = _min

    @staticmethod
    def _link_nodes(child, parent) -> None:
        """make node a child of a parent"""
        # link the child's siblings
        child.left.right = child.right
        child.right.left = child.left
        child.parent = parent

        # if parent doesn't have children, make new child its only child
        if not parent.child:
            parent.child = child.right = child.left = child
        # otherwise insert new child into parent's children list
        else:
            current_child = parent.child
            child.left = current_child
            child.right = current_child.right
            current_child.right.left = child
            current_child.right = child

        parent.degree += 1
        child.marked = False
