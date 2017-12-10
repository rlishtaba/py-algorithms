from collections import defaultdict


class HorizontalLevelOrderTraversal:
    @staticmethod
    def apply(root):
        if root is None:
            return []

        levels = defaultdict(list)
        queue = [(root, 0)]

        while len(queue) > 0:
            node, level = queue.pop()
            levels[level].append(node.element)

            if node.left is not None:
                queue.append((node.left, level - 1))

            if node.right is not None:
                queue.append((node.right, level + 1))

        return levels
