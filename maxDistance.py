# LeetCode
# maxDistance 
# Created by Yigang Zhou on 2020/9/27.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 1162. 地图分析
# https://leetcode-cn.com/problems/as-far-from-land-as-possible/
from typing import List
import collections


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        h = len(grid)
        w = len(grid[0])
        visited = set()
        q = collections.deque()

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
                    visited.add((i, j))
        if len(q) == h * w or len(q) == 0:
            return -1
        d = -1
        while q:
            print(q)
            for _ in range(len(q)):
                i, j, dist = q.popleft()
                d = dist
                for i_next, j_next in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= i_next < h and 0 <= j_next < w and (i_next, j_next) not in visited:
                        visited.add((i_next, j_next))
                        q.append((i_next, j_next, dist + 1))
        return d

grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

r = Solution().maxDistance(grid)
print(r)