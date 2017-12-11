from typing import List


class WordBreak:
    @staticmethod
    def apply(word: str, voc: List[str]) -> bool:
        queue = [0]
        visited = []

        while len(queue) > 0:
            start = queue.pop(0)
            if start not in visited:
                end = start + 1
                while end <= len(word):
                    if word[start:end] in voc:
                        queue.append(end)
                        if end == len(word):
                            return True
                    end += 1

                visited.append(start)
        return False

    @staticmethod
    def dp_apply(word: str, voc: List[str]) -> bool:
        dp = [False for _ in range(len(word))]
        length = len(word)

        for i in range(length):
            for w in voc:
                w_len = len(w)
                if w == word[i - w_len + 1:i + 1]:
                    if dp[i - w_len] or i - w_len == -1:
                        dp[i] = True
        return dp[-1]

    @staticmethod
    def dp2_apply(word: str, voc: List[str]) -> bool:
        dp = [False for _ in range(len(word) + 1)]
        dp[0] = True

        for i in range(1, len(word) + 1):
            j = 0
            while j < i:
                if dp[j] and word[j:i] in voc:
                    dp[i] = True
                j += 1

        return dp[-1]
