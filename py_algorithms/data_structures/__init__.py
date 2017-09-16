from typing import Any
from typing import List

from .deque import _DoublyLinkedListDeque
from .deque import Deque

__all__ = ['new_deque', 'Deque']


def new_deque(collection: List[Any] = ()) -> Deque:
    return _DoublyLinkedListDeque(collection)
