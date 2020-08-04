# 矩阵置零
# https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvmy42/

from typing import List
import common.arrayCommon as Array

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not len(matrix) or not len(matrix[0]):
            return

        set_i = set()
        set_j = set()
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    set_i.add(i)
                    set_j.add(j)

        for i in range(m):
            for j in range(n):
                if i in set_i or j in set_j:
                    matrix[i][j] = 0



m = [
    [0, 1, 2, 0],
    [3, 0, 5, 2],
    [1, 3, 1, 5]
]

r = Solution().setZeroes([])
Array.print2DArray(m)
