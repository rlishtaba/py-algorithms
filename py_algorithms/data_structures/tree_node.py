from typing import Any


class TreeNode:
    __slots__ = '_left', '_right', '_element'

    def __init__(self, left, right, element=None):
        self._right = right
        self._left = left
        self._element = element

    @property
    def left(self) -> 'TreeNode':
        return self._left

    def set_left(self, node: 'TreeNode') -> 'TreeNode':
        self._left = node
        return self

    @property
    def right(self) -> 'TreeNode':
        return self._right

    def set_right(self, node: 'TreeNode') -> 'TreeNode':
        self._right = node
        return self

    @property
    def element(self) -> Any:
        return self._element

    def __repr__(self):
        return "#<{} e={} left={} right={}>" \
            .format(self.__class__.__name__, self.element, self.left, self.right)
