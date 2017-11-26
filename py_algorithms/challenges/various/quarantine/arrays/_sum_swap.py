from typing import List
from typing import Union


def get_target(array1, array2):
    sum1 = sum(array1)
    sum2 = sum(array2)

    if (sum1 - sum2) % 2 != 0:
        return None
    return (sum1 - sum2) // 2


def algorithm(array1, array2) -> Union[None, List[tuple]]:
    target = get_target(array1, array2)
    if target is None:
        return None
    solutions = []
    for x in array1:
        for y in array2:
            if x - y == target:
                pair = (x, y,)
                if pair not in solutions:
                    solutions.append(pair)
    return solutions


if __name__ == '__main__':
    assert algorithm([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]) == [(4, 6), (1, 3)]
