from typing import List

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/50/sorting-and-searching/96/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums)
        for i in range(1,len(nums)):
            # if nums[i-1] >= nums[i]:
            j = i - 1
            while j > 0 and nums[j] > nums[i]:
                self.swap(nums, i, j)
                j -= 1
        print(nums)


    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp



r = Solution().sortColors([2,0,2,1,1,0])