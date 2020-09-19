# LeetCode
# integerBreak 
# Created by Yigang Zhou on 2020/9/19.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 343. 整数拆分
# https://leetcode-cn.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            m = 0
            print(dp)
            for j in range(1, i // 2 + 1):
                print(i, '可以分成', j, i - j,'dp', dp[i - j] * dp[j], dp[i - j] * j, i - j * dp[j], j * (i - j))
                # 5 -> 2的最大成绩 * 整数3 / 2整数 * 3的最大乘积 / 1 * 4的最大乘积 / 1最大乘积 * 整数4
                # m, 两个最大乘积，一个最大乘积一个自身(2种),两个整数自身
                m = max(m, dp[i - j] * dp[j], dp[i - j] * j, i - j * dp[j], j * (i - j))
            dp[i] = m
        print(dp)
        return dp[-1]


r = Solution().integerBreak(10)
