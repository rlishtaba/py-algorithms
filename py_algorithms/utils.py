from typing import Union


def compare_ints(a, b) -> Union[None, int]:
    if a < b:
        return -1
    if a > b:
        return 1
    if a == b:
        return 0
    return None
