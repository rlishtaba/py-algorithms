import abc
from typing import List


class Sort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sort(self, xs: List[int]) -> List[int]:
        raise NotImplemented()
