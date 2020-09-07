# LeetCode
# cuttingRope 
# Created by Yigang Zhou on 2020/9/6.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 剪绳子
# https://leetcode-cn.com/problems/jian-sheng-zi-lcof/


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        elif n == 3:
            return 2  # 1 * 2

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for i in range(4, n+1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], dp[j] * dp[i - j])
        return dp[-1]

s = Solution().cuttingRope(5)
print(s)