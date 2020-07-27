from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums) - 1


Solution().findPeakElement([1,2,1,3,5,6,4])