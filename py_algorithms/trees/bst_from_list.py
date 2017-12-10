from typing import Any
from typing import List
from typing import Union

from ..data_structures import new_tree_node
from ..data_structures import TreeNode


class BstFromList:
    @staticmethod
    def apply(xs: List[Any]) -> Union[TreeNode, None]:
        return BstFromList._apply(xs, 0, len(xs) - 1)

    @staticmethod
    def _apply(xs: List[Any], lo: int, hi: int) -> Union[TreeNode, None]:
        if lo > hi:
            return None

        mid = (lo + hi) // 2

        root = new_tree_node(element=xs[mid])
        root.set_left(BstFromList._apply(xs, lo, mid - 1))
        root.set_right(BstFromList._apply(xs, mid + 1, hi))

        return root
