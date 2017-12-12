from collections import OrderedDict
from typing import Any
from typing import Union


class LruCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.n = capacity
        self.table = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.table:
            node = self.table[key]
            self._remove(node)
            self._make_head(node)
            return node.value

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.table:
            node = self.table.get(key)
            node.value = value
            self._remove(node)
            self._make_head(node)
        else:
            new_node = self.Node(key, value)
            if len(self.table) >= self.n:
                del self.table[self.tail.key]
                self._remove(self.tail)
            self._make_head(new_node)
            self.table[key] = new_node

    def _remove(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def _make_head(self, node):
        node.next = self.head
        node.prev = None

        if self.head is not None:
            self.head.prev = node

        self.head = node

        if self.tail is None:
            self.tail = self.head


class SimpleLruCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key) -> Union[Any, int]:
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            value = self.d[key]
            del self.d[key]
            self.d[key] = value
            return value
        else:
            return -1

    def put(self, key, value) -> None:
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.d:
            del self.d[key]
        elif len(self.d) == self.capacity:
            self.d.popitem(False)

        self.d[key] = value
