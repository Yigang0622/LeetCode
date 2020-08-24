# LeetCode
# longestConsecutive 
# Created by Yigang Zhou on 2020/8/23.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 最长连续序列
# https://leetcode-cn.com/problems/longest-consecutive-sequence/
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_consecutive = 0
        for each in nums:
            current_consecutive = 1
            while each + 1 in num_set:
                current_consecutive += 1
                each += 1
            if current_consecutive > longest_consecutive:
                longest_consecutive = current_consecutive

        return longest_consecutive

nums = [100, 4, 200, 1, 3, 2]
s = Solution().longestConsecutive(nums)
print(s)
