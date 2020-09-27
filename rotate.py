# LeetCode
# rotate 
# Created by Yigang Zhou on 2020/9/24.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        w = len(matrix)

        # 转置
        for i in range(w):
            for j in range(w):
                if i < j:
                    temp = matrix[j][i]
                    matrix[j][i] = matrix[i][j]
                    matrix[i][j] = temp

        # 按列反转
        for i in range(w):
            j = 0
            while j <= w//2 - 1:
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][w - j - 1]
                matrix[i][w - j- 1] = temp
                j += 1


        print(matrix)


matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
s = Solution().rotate(matrix)