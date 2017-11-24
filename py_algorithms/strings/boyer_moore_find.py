class BoyerMooreFind:
    def __call__(self, string, substring) -> int:
        """

        :param string: a string to perform search in.
        :param substring: a string to find in a target.
        :return: index of start position if match found, otherwise -1.
        """

        n = len(string)
        m = len(substring)

        if m == 0:
            return 0

        last = {}
        for k in range(0, m):
            last[substring[k]] = k

        i = m - 1
        k = m - 1

        while i < n:
            if string[i] == substring[k]:
                if k == 0:
                    return i
                else:
                    i -= 1
                    k -= 1
            else:
                j = last.get(string[i], -1)
                i += m - min(k, j + 1)
                k = m - 1

        return -1
