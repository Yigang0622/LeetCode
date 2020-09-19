# LeetCode
# minFallingPathSum 
# Created by Yigang Zhou on 2020/9/19.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 下降路径最小和
# https://leetcode-cn.com/problems/minimum-falling-path-sum/
from typing import List


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        h = len(A)
        w = len(A[0])
        for i in range(1,h):
            for j in range(w):
                if j == 0:
                    A[i][j] = min(A[i-1][j] + A[i][j],A[i-1][j+1] + A[i][j])
                elif j == w - 1:
                    A[i][j] = min(A[i-1][j-1] + A[i][j],A[i-1][j] + A[i][j])
                else:
                    A[i][j] = min(A[i-1][j-1] + A[i][j],A[i-1][j] + A[i][j],A[i-1][j+1] + A[i][j])

            print(A)
        return min(A[-1])
A = [[51,24],[-50,82]]
r = Solution().minFallingPathSum(A)
print(r)