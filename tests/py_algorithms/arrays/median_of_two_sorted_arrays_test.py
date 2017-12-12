from py_algorithms.array.median_of_two_sorted_arrays import MedianOfTwoSortedArrays


class TestMedianOfTwoSortedArrays:
    def test_apply(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected_median = 2.5
        f = MedianOfTwoSortedArrays.apply
        median = f(nums1, nums2)
        assert expected_median == median

    def test_apply2(self):
        nums1 = []
        nums2 = [1]
        expected_median = 1.0
        f = MedianOfTwoSortedArrays.apply
        median = f(nums1, nums2)
        assert expected_median == median

    def test_apply3(self):
        nums1 = [1, 3]
        nums2 = [2]
        expected_median = 2.0
        f = MedianOfTwoSortedArrays.apply
        median = f(nums1, nums2)
        assert expected_median == median

    def test_apply4(self):
        nums1 = []
        nums2 = [1, 2, 3, 4]
        expected_median = 2.5
        f = MedianOfTwoSortedArrays.apply
        median = f(nums1, nums2)
        assert expected_median == median

    def test_apply5(self):
        nums1 = []
        nums2 = [1, 2, 3, 4, 5]
        expected_median = 3
        f = MedianOfTwoSortedArrays.apply
        median = f(nums1, nums2)
        assert expected_median == median
