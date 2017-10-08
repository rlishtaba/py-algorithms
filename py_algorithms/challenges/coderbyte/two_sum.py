from typing import List


class TwoSum:
    def __call__(self, xs: List[int], lookup: int) -> List[int]:
        """
        Coderbyte: Two sum problem
        Origin: https://coderbyte.com/algorithm/two-sum-problems

        Classic Two Sum problem.
        :param xs: list to perform lookup
        :param lookup: an integer value to sum with
        :return: list of pairs discovered
        """
        cache = {}
        sums = []
        for x in xs:
            desired = lookup - x
            if cache.get(desired, False):
                sums.append([x, desired])
            cache[x] = x

        return sums
