# LeetCode
# threeSun 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List

# 三数之和
# https://leetcode-cn.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        print(nums)
        self.search([], nums, 0)


    def search(self, current, nums, i):

        if i >= len(nums):
            return

        if sum(current) == 0 and len(current) == 3:
            print(current)
            return

        for j in range(i, len(nums)):
            current.append(nums[j])
            self.search(current, nums, i+1)
            current.pop()


Solution().threeSum([-1, 0, 1, 2, -1, -4])


