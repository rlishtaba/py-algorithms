from typing import Generic
from typing import List
from typing import TypeVar
from typing import Union

from . import DoublyLinkedListDeque

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self, collection: List[T]):
        self._deque = DoublyLinkedListDeque(collection)  # type: Deque

    @property
    def next(self) -> Union[None, T]:
        return self._deque.back

    def push(self, val: T) -> T:
        return self._deque.push_back(val)

    def pop(self) -> Union[None, T]:
        return self._deque.pop_back()

    @property
    def size(self) -> int:
        return self._deque.size

    def is_empty(self) -> bool:
        return self._deque.is_empty()
