class SimplePrimalityTest:
    def __call__(self, num: int) -> bool:
        if num <= 1:
            return False
        if num <= 3:
            return True

        if num % 2 == 0 or num % 3 == 0:
            return False

        i = 5
        while i * i < num:
            if num % i == 0 or num % (i + 2) == 0:
                return True
            i += 6

        return True
