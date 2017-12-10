import pytest

from py_algorithms.lists import new_singly_linked_node
from py_algorithms.lists import Node
from py_algorithms.lists.merge_two_sorted import MergeTwoSorted


@pytest.fixture
def set_nodes(xs: Node, upto: int):
    i = 1
    while i < upto:
        xs.next = new_singly_linked_node(xs.data + 1)
        xs = xs.next
        i += 1


class TestMergeTwoSorted:
    def test_apply(self):
        a = new_singly_linked_node(-7)
        b = new_singly_linked_node(1)

        a.next = new_singly_linked_node(2)
        a.next.next = new_singly_linked_node(4)

        b.next = new_singly_linked_node(3)
        b.next.next = new_singly_linked_node(5)
        b.next.next.next = new_singly_linked_node(7)

        # expected = a.next = b

        merged = MergeTwoSorted.apply(a, b)
        xs = []
        head = merged
        while head is not None:
            xs.append(head.data)
            head = head.next
        assert xs == [-7, 1, 2, 3, 4, 5, 7]
