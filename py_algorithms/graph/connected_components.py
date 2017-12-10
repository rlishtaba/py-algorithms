class UnionFind(object):
    def __init__(self, n):
        self._set = list(range(n))
        self.count = n

    def find_set(self, x):
        if self._set[x] != x:
            # path compression
            self._set[x] = self.find_set(self._set[x])
        return self._set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root != y_root:
            self._set[min(x_root, y_root)] = max(x_root, y_root)
            self.count -= 1


class ConnectedComponents:
    @staticmethod
    def apply(n, edges):
        union_find = UnionFind(n)
        for i, j in edges:
            union_find.union_set(i, j)
        return union_find.count
