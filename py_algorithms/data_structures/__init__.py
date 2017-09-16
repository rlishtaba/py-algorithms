from typing import Any
from typing import List

from .deque import Deque
from .doubly_linked_list_deque import DoublyLinkedListDeque
from .queue import Queue
from .queue import T

__all__ = [
    'new_deque',
    'Deque',
    'new_queue',
    'Queue']


def new_deque(collection: List[Any] = ()) -> Deque:
    return DoublyLinkedListDeque(collection)


def new_queue(collection: List[T] = ()) -> Queue[T]:
    return Queue[T](collection)
