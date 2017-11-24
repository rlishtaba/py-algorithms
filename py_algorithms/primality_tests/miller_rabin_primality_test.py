from random import randrange


class MillerRabinPrimalityTest:
    def __call__(self, n: int, k: int = 10) -> bool:
        if n == 2:
            return True
        if not n & 1:
            return False

        def check(a, s, d, n):
            x = pow(a, d, n)
            if x == 1:
                return True
            for i in range(0, s - 1):
                if x == n - 1:
                    return True
                x = pow(x, 2, n)
            return x == n - 1

        s = 0
        d = n - 1

        while d % 2 == 0:
            d >>= 1
            s += 1

        for _ in range(0, k):
            a = randrange(2, n)
            if not check(a, s, d, n):
                return False
        return True
