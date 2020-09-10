# LeetCode
# maximalSquare 
# Created by Yigang Zhou on 2020/9/9.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List
import common.arrayCommon as Array


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        h = len(matrix)
        w = len(matrix[0])
        dp = [[0] * w for _ in range(h)]
        maxSideLen = 0
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = int(matrix[i][j])
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                    maxSideLen = max(maxSideLen, dp[i][j])
        return maxSideLen * maxSideLen


m = [['1', '0', '1', '0', '0'],
     ['1', '0', '1', '1', '1'],
     ['1', '1', '1', '1', '1'],
     ['1', '0', '0', '1', '0']]
s = Solution().maximalSquare(m)
print(s)