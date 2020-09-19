# LeetCode
# smallestDifference 
# Created by Yigang Zhou on 2020/9/19.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 面试题 16.06. 最小差
# https://leetcode-cn.com/problems/smallest-difference-lcci/
from typing import List


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:

        a.sort()
        b.sort()
        i = 0
        j = 0
        min_diff = float('inf')
        while i < len(a) and j < len(b):
            print(i,j,a[i] - b[j])
            min_diff = min(min_diff, abs(a[i] - b[j]))
            if a[i] < b[j]:
                i += 1
            else:
                j += 1

        return min_diff

a = [1, 3, 15, 11, 2]
b= [23, 127, 235, 19, 8]
r = Solution().smallestDifference(a, b)
print(r)