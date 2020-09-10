# 统计全为 1 的正方形子矩阵
# https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        if not len(matrix) or not len(matrix[0]):
            return 0

        h = len(matrix)
        w = len(matrix[0])
        dp = [[0] * w for _ in range(h)]
        ans = 0
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
                    ans += dp[i][j]
        return ans


matrix =[
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]
r = Solution().countSquares(matrix)
print(r)