from heapq import heappop
from heapq import heappush
from heapq import nsmallest


class MedianOfTwoSortedArrays:
    @staticmethod
    def apply_2(nums1, nums2):
        def _push_to_heap(item):
            median = _median()
            if item > median:
                heappush(min_pq, item)
            elif item < median:
                heappush(max_pq, -1 * item)
            else:
                heappush(min_pq, item)

            if abs(len(max_pq) - len(min_pq)) > 1:
                _rebalance()

        def _rebalance():
            if len(min_pq) > len(max_pq):
                heappush(max_pq, -1 * heappop(min_pq))
            else:
                heappush(min_pq, -1 * heappop(max_pq))

        def _median():
            if len(min_pq) > len(max_pq):
                return float(nsmallest(1, min_pq)[0])
            elif len(max_pq) > len(min_pq):
                return float(-1 * nsmallest(1, max_pq)[0])
            else:
                if len(min_pq) == 0 and len(max_pq) == 0:
                    return 0.0
                a = nsmallest(1, min_pq)[0]
                b = -1 * nsmallest(1, max_pq)[0]
                return (a + b) / 2

        max_pq = list()
        min_pq = list()

        while len(nums1) > 0 or len(nums2) > 0:
            if len(nums1) > 0:
                _push_to_heap(nums1.pop())

            if len(nums2) > 0:
                _push_to_heap(nums2.pop())

        return _median()

    @staticmethod
    def apply(nums1, nums2):
        arr = sorted(nums1 + nums2)
        n = len(arr)
        mid = n // 2
        if n % 2 == 0:
            return (arr[mid - 1] + arr[mid]) / 2
        else:
            return float(arr[mid])
