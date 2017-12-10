from ..data_structures import TreeNode


class InOrderTraversal:
    @staticmethod
    def apply(root: TreeNode):
        xs = []
        stack = [(root, False)]

        while len(stack) > 0:
            node, is_visited = stack.pop()

            if node is None:
                continue

            if is_visited:
                xs.append(node.element)

            else:
                """ visiting right node first in order to put values on stack in ASC"""
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))

        return xs
