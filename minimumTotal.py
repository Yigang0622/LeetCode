# LeetCode
# minimumTotal 
# Created by Yigang Zhou on 2020/9/22.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 120. 三角形最小路径和
# https://leetcode-cn.com/problems/triangle/
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        h = len(triangle)
        for i in range(1, h):
            for j in range(len(triangle[i])):
                a = float('inf')
                b = float('inf')
                if 0 <= j < len(triangle[i - 1]):
                    a = triangle[i][j] + triangle[i - 1][j]
                if 0 <= j-1 < len(triangle[i-1]):
                    b = triangle[i][j] + triangle[i - 1][j - 1]
                triangle[i][j] = min(a, b)
        print(triangle)
        return min(triangle[-1])


triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

r = Solution().minimumTotal(triangle)
print(r)
