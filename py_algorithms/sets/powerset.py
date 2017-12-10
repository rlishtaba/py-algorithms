from typing import Any
from typing import List


class PowerSet:
    @staticmethod
    def apply(xs: List[Any]) -> List[Any]:
        result = []
        cardinality = 1 << len(xs)
        i = 0
        while i < cardinality:
            stack = []
            for j in range(0, len(xs)):
                if 0 != i & 1 << j:
                    stack.append(xs[j])
            result.append(stack)
            i += 1

        return result
