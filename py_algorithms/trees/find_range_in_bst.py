from py_algorithms.data_structures.tree_node import TreeNode


class FindRangeInBst:
    @classmethod
    def apply(cls, root: TreeNode, k1: int, k2: int):
        return cls._in_order_traversal(root, k1, k2)

    @classmethod
    def _in_order_traversal(cls, x: TreeNode, k1: int, k2: int):
        xs = []
        stack = [(x, False)]
        while len(stack) > 0:
            node, is_visited = stack.pop()

            if node is None:
                continue

            if is_visited:
                if node.element > k2:
                    break
                if k1 <= node.element <= k2:
                    xs.append(node.element)

            else:
                """ visiting right node first in order to put values on stack in ASC"""
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
        return xs
