from typing import List

from .power_set import PowerSet


class SubsetSum:
    def __call__(self, xs: List[int], lookup: int, power_set_f=PowerSet()) -> List[int]:
        """
        Coderbyte: Subset sum problem
        Origin: https://coderbyte.com/algorithm/subset-sum-problem-revised
        Warning: this is fast growing 2^N function

        :param xs: domain for operations
        :param lookup: an value of a sum operation
        :param power_set_f: is a function to make a power-set
        :return: sub sets where all entries summing to :lookup param
        """
        power_set = power_set_f(xs)
        occurrences = []
        for array in power_set:
            if sum(array) == lookup:
                occurrences.append(array)
        return occurrences
