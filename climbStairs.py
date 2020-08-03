# 爬楼梯
# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn854d/


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


r = Solution().climbStairs(9)
print(r)