# LeetCode
# transpose 
# Created by Yigang Zhou on 2020/9/19.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 867. 转置矩阵
# https://leetcode-cn.com/problems/transpose-matrix/
from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        h = len(A)
        w = len(A[0])
        T = [[0] * h for _ in range(w)]
        for i in range(h):
            for j in range(w):
                T[j][i] = A[i][j]
        return T


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r = Solution().transpose(A)
print(r)
