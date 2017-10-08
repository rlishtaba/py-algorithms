import math
from typing import List


class PowerSet:
    def __call__(self, xs: List[int]) -> List[List[int]]:
        """
        Coderbyte: Print all subsets (power set) of a given set
        Origin: https://coderbyte.com/algorithm/print-all-subsets-given-set

        Warning: this is fast growing 2^N function
        :param xs: list of distinct numbers
        :return: all permutations of a list
        """
        sets = []
        should_have = int(math.pow(2, len(xs)))
        for i in range(0, should_have):
            accumulator = []
            mapping = "{0:b}".format(i).rjust(len(xs), '0')
            for j in range(0, len(mapping)):
                if mapping[j] == '1':
                    accumulator.append(xs[j])
            sets.append(accumulator)
        return sets
