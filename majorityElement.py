# LeetCode
# majorityElement 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.
# https://leetcode-cn.com/explore/interview/card/top-interview-questions/264/array/1127/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]

s = Solution().majorityElement([2,2,1,1,1,2,2])
print(s)