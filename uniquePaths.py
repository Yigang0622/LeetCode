# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/51/dynamic-programming/105/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if m == 0 or n == 0:
            return 0

        dp = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

r = Solution().uniquePaths(7,3)
print(r)