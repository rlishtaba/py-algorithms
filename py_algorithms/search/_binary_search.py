from typing import List
from typing import Union

from .search import Search


class _BinarySearch(Search):
    def search(self, collection: List[int], item: int) -> Union[None, int]:
        # return early on null pointer
        if item is None:
            return None
        low = 0
        hi = len(collection) - 1
        while low <= hi:
            mid = (low + hi) // 2
            attempt = collection[mid]

            if attempt > item:
                hi = mid - 1
            elif attempt < item:
                low = mid + 1
            else:
                return attempt
        # At this point item does not exist in
        # given collection
        return None
