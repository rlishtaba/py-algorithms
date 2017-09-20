from typing import Any
from typing import List
from typing import Union

from .heap import Heap


class MinHeap(Heap):
    def __init__(self, xs: List[Any] = ()):
        super().__init__(lambda x, y: (x > y) - (x < y) == -1, xs)

    @property
    def min(self) -> Union[None, Any]:
        return self.next
