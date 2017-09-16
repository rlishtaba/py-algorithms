import abc
from typing import Any
from typing import Union


class Deque(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def size(self) -> int:
        pass

    @abc.abstractmethod
    def clear(self) -> int:
        pass

    @abc.abstractmethod
    def is_empty(self) -> bool:
        pass

    @abc.abstractproperty
    def front(self) -> Union[None, Any]:
        pass

    @abc.abstractproperty
    def back(self) -> Union[None, Any]:
        pass

    @abc.abstractproperty
    def push_front(self, val: Any) -> Any:
        pass

    @abc.abstractproperty
    def pop_front(self) -> Union[None, Any]:
        pass

    @abc.abstractproperty
    def pop_back(self) -> Union[None, Any]:
        pass

    @abc.abstractproperty
    def push_back(self, val: Any) -> Any:
        pass
