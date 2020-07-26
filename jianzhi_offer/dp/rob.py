# LeetCode
# class Solution:     def rob(self, nums: List[int]) -> int: 
# Created by Yigang Zhou on 2020/7/22.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return max(dp)

r= Solution().rob([2,1,1,5])
print(r)

