# LeetCode
# maxSubArray 
# Created by Yigang Zhou on 2020/7/22.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_sum = nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(max_sum + nums[i], nums[i])
            max_sum = dp[i]
        print(dp)
        return max(dp)

Solution().maxSubArray([-1,-2])

