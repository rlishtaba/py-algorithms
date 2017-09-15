import abc
from typing import List
from typing import Union


class Search(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def search(self, collection: List[int], item: int) -> Union[None, int]:
        pass
