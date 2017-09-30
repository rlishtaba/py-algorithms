import abc
from typing import Any
from typing import List


class Sort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sort(self, xs: List[int]) -> List[int]:
        raise NotImplemented()

    @staticmethod
    def _test_iterable(xs: Any):
        if not isinstance(xs, (list, tuple)):
            raise RuntimeError('Can sort only iterable entity.')
