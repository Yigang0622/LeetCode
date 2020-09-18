from typing import List


# 岛屿的最大面积
# https://leetcode-cn.com/problems/max-area-of-island/

class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        h = len(grid)
        w = len(grid[0])

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:

                    maxArea = max(self.countArea(grid, i, j, w, h), maxArea)

        return maxArea

    def countArea(self, grid, i, j, w, h):
        if i < 0 or i >= h or j < 0 or j >= w:
            return 0
        if grid[i][j] == 0:
            return 0
        ans = 1
        grid[i][j] = 0
        for i_next, j_next in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            ans += self.countArea(grid, i_next, j_next, w, h)
        return ans


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

r = Solution().maxAreaOfIsland(grid)
print(r)
