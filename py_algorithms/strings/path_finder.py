class PathFinder:
    def __call__(self, matrix, position, n, m):
        if position == (n - 1, m - 1):
            return [(n - 1, m - 1)]

        x, y = position
        if x + 1 < n and matrix[x + 1][y] == 1:
            a = self(matrix, (x + 1, y), n, m)
            if a is not None:
                return [(x, y)] + a
        if y + 1 < m and matrix[x][y + 1] == 1:
            b = self(matrix, (x, y + 1), n, m)
            if b is not None:
                return [(x, y)] + b


if __name__ == '__main__':
    algorithm = PathFinder()
    mat = [
        [1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 0, 0, 1, 1],
        [1, 0, 0, 1, 1]
    ]
    print(algorithm(mat, (0, 0), len(mat), len(mat[0])))
