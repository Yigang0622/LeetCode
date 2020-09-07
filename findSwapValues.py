# LeetCode
# findSwapValues 
# Created by Yigang Zhou on 2020/9/3.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 交换和
# https://leetcode-cn.com/problems/sum-swap-lcci/
from typing import List


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        sum1 = sum(array1)
        sum2 = sum(array2)

        s1 = set(array1)
        s2 = set(array2)

        # sum1 - a + b = sum2 - b + a
        # sum1 - sum2 = 2a - 2b
        # b = -(sum1 - sum2 - 2a) / 2
        for each in s1:
            target = -(sum1 - sum2 - 2*each) // 2
            if target in s2:
                return [each, target]
        return []

array1 = [1,2,3]
array2 = [4,5,6]
r = Solution().findSwapValues(array1, array2)
print(r)