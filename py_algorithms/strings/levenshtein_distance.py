from typing import Any
from typing import List


class LevenshteinDistance:
    @classmethod
    def apply(cls, a: List[Any], b: List[Any]) -> int:
        matrix = [[-1 for _ in range(len(b))] for _ in range(len(a))]
        return cls._compute_distance_on_prefixes(a, b, len(a) - 1, len(b) - 1, matrix)

    @classmethod
    def _compute_distance_on_prefixes(cls, a, b, i: int, j: int, matrix) -> int:
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        if matrix[i][j] == -1:
            if a[i] == b[j]:
                matrix[i][j] = cls._compute_distance_on_prefixes(
                    a, b, i - 1, j - 1, matrix)
            else:
                sub_last = cls._compute_distance_on_prefixes(
                    a, b, i - 1, j - 1, matrix)
                add_last = cls._compute_distance_on_prefixes(
                    a, b, i - 1, j, matrix)
                del_last = cls._compute_distance_on_prefixes(
                    a, b, i, j - 1, matrix)
                matrix[i][j] = 1 + min(sub_last, add_last, del_last)

        return matrix[i][j]
