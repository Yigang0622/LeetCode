# LeetCode
# countServers 
# Created by Yigang Zhou on 2020/9/27.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 1267. 统计参与通信的服务器
# https://leetcode-cn.com/problems/count-servers-that-communicate/
from typing import List
import common.arrayCommon as Array


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        count = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    c = self.dfs(i, j, w, h, grid)
                    if c != 1:
                        count += c
        return count

    def dfs(self, i, j, w, h, grid):
        count = 0
        for y in range(h):
            if grid[y][j] == 1:
                grid[y][j] = 2
                count += 1 + self.dfs(y, j, w, h, grid)
        for x in range(w):
            if grid[i][x] == 1:
                grid[i][x] = 2
                count += 1 + self.dfs(i, x, w, h, grid)
        return count


grid = [[0,0,0,1,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0]]
Array.print2DArray(grid)
r = Solution().countServers(grid)
print()
Array.print2DArray(grid)

print(r)
