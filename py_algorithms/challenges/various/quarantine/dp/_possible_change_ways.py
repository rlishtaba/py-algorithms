from typing import List


def _make_change(amount: int, denoms: List[int], index: int, cache) -> int:
    if amount in cache:
        if index in cache[amount]:
            return cache[amount][index]

    if index >= len(denoms) - 1:
        return 1

    denom_amount = denoms[index]
    ways = 0
    i = 1
    while i * denom_amount <= amount:
        remaining = amount - i * denom_amount
        ways += _make_change(remaining, denoms, index + 1, cache)
        i += 1
    if amount not in cache:
        cache[amount] = {}
    cache[amount][index] = ways

    return ways


def make_change(amount, denoms: List[int]):
    cache = {}
    ways = _make_change(amount, denoms, 0, cache)
    return ways


if __name__ == '__main__':
    assert make_change(100, [1, 5, 10, 25]) == 2625
