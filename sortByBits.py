# LeetCode
# sortByBits 
# Created by Yigang Zhou on 2020/11/7.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 1356. 根据数字二进制下 1 的数目排序
# https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/
from typing import List

class MyNumber:

    def __init__(self, val):
        self.val = val
        self.count = self._numberOfOneBits(val)

    def _numberOfOneBits(self, val):
        count = 0
        while val > 0:
            if val & 1:
                count += 1
            val = val >> 1
        return count

    def __lt__(self, other):
        if other.count == self.count:
            return other.val > self.val
        return other.count > self.count


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        my_nums = [MyNumber(x) for x in arr]
        my_nums.sort()
        return [x.val for x in my_nums]

arr = [0,1,2,3,4,5,6,7,8]
r = Solution().sortByBits(arr)
print(r)