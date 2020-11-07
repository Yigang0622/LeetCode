# LeetCode
# numTrees 
# Created by Yigang Zhou on 2020/10/31.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 96. 不同的二叉搜索树
# https://leetcode-cn.com/problems/unique-binary-search-trees/


class Solution:

    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        # print(dp)
        for i in range(2, n+1):
            # 1 2 3 的时候分别计算 1 为 root，2为root，3为root的树的个数
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        # print(dp)
        return dp[-1]

s = Solution().numTrees(8)