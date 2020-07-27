from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        for i in range(2, len(nums)):
            if nums[i-2] < nums[i-1] and nums[i-1] < nums[i] and nums[i-2] < nums[i]:
                return True
        return False

