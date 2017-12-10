from typing import List


class GenBinStringsWithNBits1:
    def __call__(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ['0', '1']

        xs = []

        for bitstring in self(n - 1):
            for digit in self(1):
                xs.append(digit + bitstring)

        return xs


class GenBinStringsWithNBits2:
    def __call__(self, num: int, f) -> List[str]:
        if num == 0:
            return []
        if num == 1:
            return ['0', '1']
        left = f('0', self(num - 1, f))
        right = f('1', self(num - 1, f))
        return left + right


def _append_at_beginning_front(x, xs):
    return [x + element for element in xs]


if __name__ == '__main__':
    print(GenBinStringsWithNBits1()(4))
    print(GenBinStringsWithNBits2()(4, _append_at_beginning_front))
