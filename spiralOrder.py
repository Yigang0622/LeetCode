# LeetCode
# spiralOrder 
# Created by Yigang Zhou on 2020/8/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 螺旋矩阵
# https://leetcode-cn.com/problems/spiral-matrix/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not len(matrix):
            return []

        res = []
        h = len(matrix)
        w = len(matrix[0])
        visited = [[0] * w for _ in range(h)]
        total = h * w
        direction = 'r'  # r d l u
        i = 0
        j = 0
        while total > 0:
            if i < 0 or i >= h or j < 0 or j >= w or visited[i][j] == 1:
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
            res.append(matrix[i][j])
            total -= 1
            if direction == 'r':
                j += 1
            elif direction == 'd':
                i += 1
            elif direction == 'l':
                j -= 1
            elif direction == 'u':
                i -= 1
        return res


m = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

r = Solution().spiralOrder(m)
print(r)
