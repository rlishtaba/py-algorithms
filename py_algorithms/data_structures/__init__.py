from typing import Any
from typing import Callable
from typing import List
from typing import TypeVar

from .deque import Deque
from .doubly_linked_list_deque import DoublyLinkedListDeque
from .heap import Heap
from .max_heap import MaxHeap
from .min_heap import MinHeap
from .priority_queue import PriorityQueue
from .queue import Queue
from .stack import Stack
from .suffix_array import SuffixArray

T = TypeVar('T')

__all__ = [
    'new_deque',
    'Deque',
    'new_queue',
    'Queue',
    'new_stack',
    'Stack',
    'new_heap',
    'Heap',
    'new_max_heap',
    'new_min_heap',
    'new_priority_queue',
    'PriorityQueue',
    'new_suffix_array',
]


def new_deque(collection: List[Any] = ()) -> Deque:
    """
    Generic Dequeue, doubly linked list based implementation

    :param collection: List[Any]
    :return: Deque
    """
    return DoublyLinkedListDeque(collection)


def new_queue(collection: List[T] = ()) -> Queue[T]:
    """
    Generic Queue, using Deque underneath

    :param collection: List[T]
    :return: Queue
    """
    return Queue[T](collection)


def new_stack(collection: List[T] = ()) -> Stack[T]:
    """
    Generic Stack, using Deque underneath

    :param collection: List[T]
    :return: Stack
    """
    return Stack[T](collection)


def new_heap(comparator_f2: Callable[[Any, Any], bool], xs: List[Any] = ()) -> Heap:
    """
        Fibonacci Heap

    Factory method to construct generic heap
    :param comparator_f2: a morphism to apply in order to compare heap entries
    :param List[T] xs: a list of initial isomorphic values to populate heap
    :return: pointer to Heap interface

    Example of a generic Max heap

    >>> max_heap = new_heap(lambda x, y: (x > y) - (x < y) == 1)
    >>> max_heap.push('Kelly', 1)
    >>> max_heap.push('Ryan', 7)
    >>> max_heap.next_key #=> 'Ryan'
    >>> max_heap.pop()    #=> 7

    """
    return Heap(comparator_f2, xs)


def new_max_heap(xs: List[Any] = ()) -> Heap:
    """
        MAX Heap (Fibonacci Heap engine)

    :param xs: optional collection of initial values
    :return: an interface to Heap
    """
    return MaxHeap(xs)


def new_min_heap(xs: List[Any] = ()) -> Heap:
    """
        MAX Heap (Fibonacci Heap engine)

    :param xs: optional collection of initial values
    :return: an interface to Heap
    """
    return MinHeap(xs)


def new_priority_queue(queue_vector_f2: Callable[[Any, Any], bool]) -> PriorityQueue:
    """
        MAX Priority Queue (Fibonacci Heap engine)

        >>> from py_algorithms.data_structures import new_priority_queue
        >>>
        >>> pq = new_priority_queue(lambda x, y: (x > y) - (x < y) == 1)
        >>> pq.push('Important', 10)
        >>> pq.push('Not So Important', -2)
        >>> pq.pop() #=> 'Important'

    :param queue_vector_f2: a functor defining queue order
    :return: a PriorityQueue interface
    """
    return PriorityQueue(queue_vector_f2)


def new_suffix_array(string: str) -> SuffixArray:
    """
    >>> from py_algorithms.data_structures import new_suffix_array
    >>>
    >>> ds = new_suffix_array('python')
    >>> ds.is_sub_str('py') #=> True
    >>> ds.is_sub_str('on') #=> True
    >>> ds.is_sub_str('ton') #=> True
    >>> ds.is_sub_str('blah') #=> False

    :param string: a subject for detection
    :return: SuffixArray interface
    """
    return SuffixArray(string)
