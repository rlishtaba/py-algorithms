from .node import Node


class FindMergePoint:
    @staticmethod
    def apply(a: Node, b: Node) -> Node:
        head_a = a
        head_b = b
        i = 0
        while head_a != head_b:
            if head_a.next is None:
                head_a = b
            else:
                head_a = head_a.next

            if head_b.next is None:
                head_b = a
            else:
                head_b = head_b.next
            i += 1
            print(i)

        return head_b
