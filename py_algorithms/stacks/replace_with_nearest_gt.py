from typing import Any
from typing import List


class ReplaceWithNearestGreatest:
    @staticmethod
    def apply(xs: List[Any]) -> List[Any]:
        result = []
        stack = [xs[0]]
        for i in range(0, len(xs)):
            nearest_gt = xs[i]
            if len(stack) > 0:
                element = stack.pop()
                while element < nearest_gt:
                    result.append(nearest_gt)
                    if len(stack) == 0:
                        break
                    element = stack.pop()
                if element > nearest_gt:
                    stack.append(element)
            stack.append(nearest_gt)

        while len(stack) > 0:
            stack.pop()
            result.append(float('inf'))

        return result


if __name__ == '__main__':
    f = ReplaceWithNearestGreatest()
    _xs = [0, 0, 1, 0, 3, 0, 4]
    assert f.apply(_xs) == [1, 3, 3, 4, 4, float('inf')]
