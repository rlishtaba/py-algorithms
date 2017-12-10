__all__ = [
    'Node',
    'new_singly_linked_node',
    'merge_linked_lists',
]

from .node import Node
from .merge_two_sorted import MergeTwoSorted


def new_singly_linked_node(data, successor=None):
    return Node(data, successor)


def merge_linked_lists(a: Node, b: Node) -> Node:
    return MergeTwoSorted.apply(a, b)
