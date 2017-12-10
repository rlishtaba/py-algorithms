import pytest

from py_algorithms.lists import new_singly_linked_node
from py_algorithms.lists import Node
from py_algorithms.lists.find_merge_point import FindMergePoint


@pytest.fixture
def set_nodes(xs: Node, upto: int):
    i = 1
    while i < upto:
        xs.next = new_singly_linked_node(xs.data + 1)
        xs = xs.next
        i += 1


class TestFindMergePoint:
    def test_apply(self):
        a = new_singly_linked_node(0)
        b = new_singly_linked_node(6)

        set_nodes(a, 5)
        set_nodes(b, 5)

        merge_point = b.next.next
        a.next.next.next = merge_point

        discovered_point = FindMergePoint.apply(a, b)
        assert discovered_point == merge_point

    def test_is_even(self):
        a = new_singly_linked_node(0)
        set_nodes(a, 6)
        b = new_singly_linked_node(0)
        set_nodes(b, 5)

        def is_even(xs: Node) -> bool:
            current = xs
            while current is not None and current.next is not None:
                current = current.next.next
                if current is None:
                    return True
            return False

        assert is_even(a) is True
        assert is_even(b) is False
