from typing import Any


class Vertex:
    __slots__ = '_element'

    def __init__(self, element: Any):
        self._element = element

    def element(self) -> Any:
        return self._element

    def __hash__(self) -> int:
        return hash(id(self))

    def __repr__(self):
        return "#<{}({})>" \
            .format(self.__class__.__name__, self.element())
