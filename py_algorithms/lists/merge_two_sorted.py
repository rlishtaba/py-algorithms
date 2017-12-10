from .node import Node


class MergeTwoSorted:
    @staticmethod
    def apply(a: Node, b: Node) -> Node:
        ptr = Node(-1, None)
        head = ptr
        while a is not None and b is not None:

            if a.data < b.data:
                head.next = a
                a = a.next
            else:
                head.next = b
                b = b.next

            head = head.next

        if a:
            head.next = a

        if b:
            head.next = b

        return ptr.next
