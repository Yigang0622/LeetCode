# LeetCode
# longestSubsequence 
# Created by Yigang Zhou on 2020/9/21.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 最长定差子序列
# https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference/
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = dict()
        ans = 1

        for each in arr:
            if each - difference in dp:
                dp[each] = dp[each - difference] + 1
            else:
                dp[each] = 1
            ans = max(ans, dp[each])

        return ans

arr = [1,5,7,8,5,3,4,2,1]
difference = -2
r = Solution().longestSubsequence(arr, difference)
print(r)

