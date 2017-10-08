class LoveLetterMystery:

    def __call__(self, word):
        """
        Hackerrank challenge: The Love-Letter Mystery
        Original description:
            https://www.hackerrank.com/challenges/the-love-letter-mystery/problem

        For the actual tests see: tests/py_algorithms/various/hackerrank module

        :param word: a word to mutate
        :return: count of ops to mutate
        """
        ops = []
        low = 0
        hi = len(word)
        median = hi // 2
        for i in range(low, median):
            ops.append(abs(ord(word[i]) - ord(word[hi - 1 - i])))
        return sum(ops)
