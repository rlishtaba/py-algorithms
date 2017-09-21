import copy

from ..utils import three_way_cmp


class SuffixArray:
    def __init__(self, string: str):
        if not string:
            raise RuntimeError('Could not work with Nothing.')
        as_string = str(string)
        self._original = copy.copy(as_string)
        self._suffixes = []
        for i in range(0, len(as_string)):
            self._suffixes.append(as_string[i:])
        self._suffixes = sorted(self._suffixes)

    def is_sub_str(self, a_string: str) -> bool:
        if not a_string:
            return False
        string = str(a_string)
        substring_length = len(string)
        if substring_length < 1:
            return False
        low, hi = 0, len(self._suffixes) - 1
        while low <= hi:
            mid = (low + hi) // 2
            suffix = self._suffixes[mid][0:substring_length]
            res = three_way_cmp(string, suffix)
            if res == 0:
                return True
            if res == 1:
                low = mid + 1
            else:
                hi = mid - 1
        return False
