from typing import Any
from typing import Tuple
from typing import Union

from .vertex import Vertex


class Edge:
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, origin: Vertex, destination: Vertex, element: Any):
        self._element = element
        self._destination = destination
        self._origin = origin

    def endpoints(self) -> Tuple[Any, Any]:
        return self._origin, self._destination

    def opposite(self, v) -> Union[None, Vertex]:
        return self._destination if v is self._origin else self._origin

    def element(self) -> Any:
        return self._element

    def __hash__(self):
        return hash((self._origin, self._destination,))

    def __repr__(self):
        return "#<{}({}) ({},{})>" \
            .format(self.__class__.__name__,
                    self.element(),
                    self._origin.element(),
                    self._destination.element())
