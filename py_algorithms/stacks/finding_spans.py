from typing import List

from ..data_structures import new_stack


class FindingSpans:
    """

    """

    @staticmethod
    def apply(xs: List[int]):
        stack = new_stack()
        state = [float('inf') for _ in range(len(xs))]

        for i in range(0, len(xs)):
            while not stack.is_empty() and xs[i] > xs[stack.peek()]:
                stack.pop()

            if stack.is_empty():
                p = -1
            else:
                p = stack.peek()

            state[i] = i - p
            stack.push(i)
        return state


if __name__ == '__main__':
    data = [6, 3, 4, 5, 2]
    assert FindingSpans.apply(data) == []
