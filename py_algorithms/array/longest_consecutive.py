from typing import List


class LongestConsecutive:
    @staticmethod
    def apply(nums: List[int]) -> int:
        return LongestConsecutive.with_sorting(nums)

    @staticmethod
    def with_sorting(nums: List[int]):
        if not nums:
            return 0

        nums = sorted(nums)
        longest_consecutive = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current += 1
                else:
                    longest_consecutive = max(current, longest_consecutive)
                    current = 1

        return max(current, longest_consecutive)

    @staticmethod
    def brute_force(nums: List[int]):
        if not nums:
            return 0

        longest_consecutive = 1
        for num in nums:
            current = num
            current_seq = 1

            while current + 1 in nums:
                current += 1
                current_seq += 1

            longest_consecutive = max(longest_consecutive, current_seq)
        return longest_consecutive

    @staticmethod
    def with_set(nums):
        xs = set(nums)
        known_max = 0

        for p in xs:
            if p - 1 not in xs:
                q = p + 1
                while q in xs:
                    q += 1
                known_max = max(known_max, q - p)

        return known_max
