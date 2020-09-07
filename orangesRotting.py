# 腐烂的橘子
# https://leetcode-cn.com/problems/rotting-oranges/
from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()

        h = len(grid)
        w = len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 2:
                    q.append((i,j))

        time = 0
        while(q):
            for _ in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = 2
                for i_next, j_next in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=i_next<h and 0<=j_next<w and grid[i_next][j_next] == 1:
                        q.append((i_next,j_next))
            time += 1

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    return -1
        if time == 0:
            return 0
        else:
            return time - 1




grid = [[2,1,1],[1,1,0],[0,1,1]]
s = Solution()
r = s.orangesRotting(grid)
print(r)