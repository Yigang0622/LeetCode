# LeetCode
# wordBreak_dp 
# Created by Yigang Zhou on 2020/9/14.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 139. 单词拆分
# https://leetcode-cn.com/problems/word-break/
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictionary = set(wordDict)

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and (s[i:j] in dictionary):
                    # print(i,j, s[i:j])

                    dp[j] = 1

        return bool(dp[-1])


s = "applepenapple"
wordDict = ["apple", "pen"]
r = Solution().wordBreak(s, wordDict)
