# 最小路径和
# https://leetcode-cn.com/problems/minimum-path-sum/
from typing import List
from common.arrayCommon import *


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h = len(grid)
        if h == 0:
            return 0

        w = len(grid[0])
        if h == 1 and w == 1:
            return grid[0][0]

        dp = [[0 for _ in range(w)] for _ in range(h)]
        dp[0][0] = grid[0][0]

        for i in range(h):
            for j in range(w):
                if i == 0 and j != 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif i != 0 and j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
        return dp[h-1][w-1]

grid = [[1]]
r = Solution().minPathSum(grid)
print(r)