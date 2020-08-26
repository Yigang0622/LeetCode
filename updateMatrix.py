# 01矩阵
# https://leetcode-cn.com/problems/01-matrix/

from typing import List
import collections


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # 广度优先
        h = len(matrix)
        w = len(matrix[0])
        distance = [[0] * w for _ in range(h)]
        q = collections.deque()
        seen = set()
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    q.append((i, j))
                    seen.add((i, j))
        while q:
            i, j = q.popleft()
            for next_i, next_j in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                if 0 <= next_i < h and 0 <= next_j < w:
                    if (next_i, next_j) not in seen:
                        distance[next_i][next_j] = distance[i][j] + 1
                        q.append((next_i, next_j))
                        seen.add((next_i, next_j))
        return distance



m = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
r = Solution().updateMatrix(m)
