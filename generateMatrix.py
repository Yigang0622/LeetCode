# LeetCode
# generateMatrix 
# Created by Yigang Zhou on 2020/8/30.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# https://leetcode-cn.com/problems/spiral-matrix-ii/
# 螺旋矩阵2
from typing import List
import common.arrayCommon as Array


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return [[]]

        m = [[0] * n for _ in range(n)]
        visited = [[0] * n for _ in range(n)]
        count = 1
        direction = 'r'  # r d l u
        i = 0
        j = 0
        while count <= n*n:
            if i < 0 or i >= n or j < 0 or j >= n or visited[i][j] == 1:
                if direction == 'r':
                    direction = 'd'
                    j -= 1
                    i += 1
                elif direction == 'd':
                    direction = 'l'
                    i -= 1
                    j -= 1
                elif direction == 'l':
                    direction = 'u'
                    j += 1
                    i -= 1
                elif direction == 'u':
                    direction = 'r'
                    j += 1
                    i += 1

            visited[i][j] = 1
            m[i][j] = count
            count += 1
            if direction == 'r':
                j += 1
            elif direction == 'd':
                i += 1
            elif direction == 'l':
                j -= 1
            elif direction == 'u':
                i -= 1
        return m

m = Solution().generateMatrix(2)
Array.print2DArray(m)

