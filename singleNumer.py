# LeetCode
# singleNumer 
# Created by Yigang Zhou on 2020/7/22.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]
        return result

r = Solution().singleNumber([1,2,1,3,3])
print(r)
