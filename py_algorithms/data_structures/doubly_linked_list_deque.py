import abc
from typing import Any
from typing import List
from typing import Union

from . import Deque


class _Node(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def left(self) -> Union[None, '_Node']:
        pass

    @abc.abstractproperty
    def right(self) -> Union[None, '_Node']:
        pass

    @abc.abstractproperty
    def val(self) -> Any:
        pass


class DoublyLinkedListDeque(Deque):
    """
        Actual Deque implementation using doubly-linked lists
        Operations: O(1) complexity
    """

    class _NodeImpl:
        def __init__(self, left: Union[None, _Node], right: Union[None, _Node], val: Any):
            self.left = left
            self.right = right
            self.val = val

    def __init__(self, collection: List[Any] = ()):
        self._front = None  # type: _Node
        self._back = None  # type: _Node
        self._size = 0  # type: int
        # initialize deque with optional collection
        for x in collection:
            self.push_back(x)

    def is_empty(self) -> bool:
        return 0 == self.size

    def clear(self) -> int:
        self._front = None
        self._back = None
        self._size = 0
        return self.size

    @property
    def size(self) -> int:
        return self._size

    @property
    def back(self) -> Union[None, Any]:
        if self._back is not None:
            return self._back.val
        return None

    @property
    def front(self) -> Union[None, Any]:
        if self._front is not None:
            return self._front.val
        return None

    def push_front(self, val: Any) -> Any:
        node = self._NodeImpl(None, None, val)
        if self._front:
            node.right = self._front
            self._front.left = node
            self._front = node
        else:
            self._front = node
            self._back = self._front
        self._size += 1
        return val

    def push_back(self, val: Any) -> Any:
        node = self._NodeImpl(None, None, val)
        if self._back:
            node.left = self._back
            self._back.right = node
            self._back = node
        else:
            self._front = node
            self._back = self._front
        self._size += 1
        return val

    def pop_front(self) -> Union[None, Any]:
        if self._front is None:
            return None

        node = self._front

        if 1 == self.size:
            self.clear()
            return node.val
        else:
            self._front.right.left = None
            self._front = self._front.right

        self._size -= 1
        return node.val

    def pop_back(self) -> Union[None, Any]:
        if self._back is None:
            return None

        node = self._back

        if 1 == self.size:
            self.clear()
            return node.val
        else:
            self._back.left.right = None
            self._back = self._back.left

        self._size -= 1
        return node.val
