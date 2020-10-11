# LeetCode
# minNumber 
# Created by Yigang Zhou on 2020/10/10.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 剑指 Offer 45. 把数组排成最小的数
# https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/
from typing import List


class MyStr:

    def __init__(self, s):
        self.s = str(s)

    def __str__(self):
        return self.s

    def __lt__(self, other):
        return int(str(self)+str(other)) < int(str(other)+str(self))

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        if not len(nums):
            return ''
        my_str_arr = [MyStr(x) for x in nums]
        my_str_arr.sort()
        return ''.join([str(x) for x in my_str_arr])

nums = [3,30,34,5,9]
s = Solution().minNumber(nums)
print(s)