from typing import List


class ArrayAddition:
    def __call__(self, arr: List[int]) -> bool:
        max_num = max(arr)
        arr.remove(max_num)
        return self._test(arr, max_num)

    @classmethod
    def _test(cls, arr: List[int], max_num: int) -> bool:
        for x in arr:
            # Found, return early
            if x == max_num:
                return True
            # clone current list
            c_arr = list(arr)
            # remove used number
            c_arr.remove(x)
            # recur test, for target - removed value
            if cls._test(c_arr, max_num - x):
                return True
        # Target not found
        return False
