class LevelOrderTraversal:
    @staticmethod
    def apply(root):
        if root is None:
            return []

        levels = []
        queue = [root]

        while len(queue) > 0:
            level = []
            next_queue = []

            for node in queue:
                level.append(node.element)
                if node.left is not None:
                    next_queue.append(node.left)
                if node.right is not None:
                    next_queue.append(node.right)

            levels.append(level)
            queue = next_queue
        return levels
