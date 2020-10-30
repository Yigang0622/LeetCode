from typing import List

# 463. 岛屿的周长
# https://leetcode-cn.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        if not len(grid):
            return 0

        h = len(grid)
        w = len(grid[0])

        perimeter = 0

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    for i_next, j_next in [(i-1,j),(i,j-1),(i+1,j),(i, j+1)]:
                        if 0 <= i_next < h and 0 <= j_next < w:
                            if grid[i_next][j_next] == 0:
                                perimeter += 1
                        else:
                            perimeter += 1
        return perimeter


grid = [[0,1,0,0],
     [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]

s = Solution().islandPerimeter(grid)
