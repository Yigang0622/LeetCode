# LeetCode
# closedIsland 
# Created by Yigang Zhou on 2020/10/8.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List
import common.arrayCommon as array

# 1254. 统计封闭岛屿的数目
# https://leetcode-cn.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        ans = 0
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                if grid[i][j] == 0:
                    is_closed_island = self.dfs(i, j, w, h, grid)
                    # array.print2DArray(grid)
                    # print()
                    if is_closed_island:
                        ans += 1
        return ans

    def dfs(self, i, j, w, h, grid):
        if grid[i][j] == 3:
            return True
        if i == 0 or i == h - 1 or j == 0 or j == w - 1:
            if grid[i][j] == 0:
                return False
            else:
                return True
        if grid[i][j] == 1:
            return True
        grid[i][j] = 3
        up = self.dfs(i - 1, j, w, h, grid)
        down = self.dfs(i + 1, j, w, h, grid)
        left = self.dfs(i, j - 1, w, h, grid)
        right = self.dfs(i, j + 1, w, h, grid)
        return up and down and left and right


# 0陆地 1水域
grid = [[1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]]
r = Solution().closedIsland(grid)
print(r)