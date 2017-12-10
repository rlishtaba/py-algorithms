__all__ = [
    'level_order_traversal',
    'horizontal_level_order_traversal',
    'new_bst_from_list',
]
from typing import List, Any

from ..data_structures import TreeNode
from .level_order_traversal import LevelOrderTraversal
from .horizontal_level_order_traversal import HorizontalLevelOrderTraversal
from .bst_from_list import BstFromList
from .in_order_traversal import InOrderTraversal
from .find_range_in_bst import FindRangeInBst


def in_order_traversal(root: TreeNode) -> List[List[Any]]:
    """
    Factory method
    :param root: TreeNode
    :return: Result of traversal
    """
    return InOrderTraversal.apply(root)


def level_order_traversal(root: TreeNode) -> List[List[Any]]:
    """
    Factory method
    :param root: TreeNode
    :return: List of levels
    """
    return LevelOrderTraversal.apply(root)


def horizontal_level_order_traversal(root: TreeNode) -> List[List[Any]]:
    """
    Factory method
    :param root: TreeNode
    :return: List of levels
    """
    return HorizontalLevelOrderTraversal.apply(root)


def new_bst_from_list(xs: List[Any]) -> TreeNode:
    """
    Factory method
    :param xs: List of comparable objects
    :return: root Tree node
    """
    return BstFromList.apply(xs)


def find_range_in_bst(bst, k1, k2) -> List[Any]:
    """
    Factory method
    :param bst: TreeNode
    :param k1: start of the range
    :param k2: end of the range
    :return: List
    """
    return FindRangeInBst.apply(root=bst, k1=k1, k2=k2)
