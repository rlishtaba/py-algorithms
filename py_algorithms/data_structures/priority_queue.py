from typing import Any
from typing import Callable
from typing import Union

from . import Heap


class PriorityQueue:
    def __init__(self, queue_vector_f2: Callable[[Any, Any], bool]):
        self._comparator = queue_vector_f2
        self._heap = Heap(queue_vector_f2)

    @property
    def size(self):
        return self._heap.size

    @property
    def is_empty(self) -> bool:
        return self._heap.is_empty

    @property
    def next(self) -> Union[Any, None]:
        return self._heap.next

    def push(self, val: Any, priority: int) -> Any:
        """
        >>> pq = PriorityQueue(lambda x, y: (x > y) - (x < y) == 1)
        >>> pq.push('Important', 10)
        >>> pq.push('Not So Important', -2)
        >>> pq.pop() #=> 'Important'

        :param val: an object to manage
        :param priority: an integer value representing priority weight
        :return: value pushed to PQ
        """
        return self._heap.push(priority, val)

    def pop(self) -> Union[Any, None]:
        """
        >>> pq = PriorityQueue(lambda x, y: (x > y) - (x < y) == -1)
        >>> pq.push('Important', 10)
        >>> pq.push('Not So Important', -2)
        >>> pq.pop() #=> 'Not So Important'
        :return: an object managed by PQ
        """
        return self._heap.pop()

    def clear(self):
        return self._heap.clear()

    def has_priority(self, priority: int) -> bool:
        return self._heap.contains_key(priority)
