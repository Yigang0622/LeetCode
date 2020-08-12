from typing import List

# 颜色分类
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/50/sorting-and-searching/96/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums) - 1
        curr = 0
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            elif nums[curr] == 1:
                curr += 1

r = Solution().sortColors([2,0,1])
