# LeetCode
# NumMatrix 
# Created by Yigang Zhou on 2021/1/31.
# Copyright © 2021 Yigang Zhou. All rights reserved.
from typing import List

# 304. 二维区域和检索 - 矩阵不可变
# https://leetcode-cn.com/problems/range-sum-query-2d-immutable/
from common.arrayCommon import *


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        h = len(matrix)
        w = len(matrix[0])
        self.dp = [[0] * (w+1) for x in range(h+1)]
        for i in range(h):
            for j in range(w):
                self.dp[i+1][j+1] = self.dp[i+1][j] + self.dp[i][j+1] + matrix[i][j] - self.dp[i][j]

        # print2DArray(matrix)
        # print()
        # print2DArray(self.dp)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2+1][col1] + self.dp[row1][col1]
        # print(self.dp[row2 + 1][col2 + 1])
        # print(self.dp[row1][col2+1])
        # print(self.dp[row2+1][col1])
        # print(self.dp[row1][col1])
        # print(result)
        return result



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

obj = NumMatrix(matrix)
param_1 = obj.sumRegion(2,1,4,3)
param_1 = obj.sumRegion(1,2,2,4)

