# https://leetcode-cn.com/explore/interview/card/top-interview-questions/273/graph-theory/1183/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        h = len(grid)
        w = len(grid[0])
        count = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    count += 1
                    self.markIsland(i,j,grid,w,h)

        return count


    def markIsland(self,i,j,grid,w,h):
        if i < 0 or i >= h or j < 0 or j >= w:
            return
        if grid[i][j] != '1':
            return
        grid[i][j] = '-1'
        self.markIsland(i+1,j,grid,w,h)
        self.markIsland(i-1,j,grid,w,h)
        self.markIsland(i,j+1,grid,w,h)
        self.markIsland(i,j-1,grid,w,h)


grid = [['0', '1', '0', '1']]
r = Solution().numIslands(grid)
print(r)
