# LeetCode
# majorityElement2 
# Created by Yigang Zhou on 2020/10/7.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 面试题 17.10. 主要元素
# https://leetcode-cn.com/problems/find-majority-element-lcci/
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums) // 2
        nums.sort()
        counter = {}
        for each in nums:
            if each not in counter:
                counter[each] = 1
            else:
                counter[each] += 1
            if counter[each] > n:
                return each
        return -1


nums = [3,2]
r = Solution().majorityElement(nums)
print(r)
