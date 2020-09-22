
# 300. 最长上升子序列
# https://leetcode-cn.com/problems/longest-increasing-subsequence/
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)


        print(dp)
        return max(dp)

nums = [10 ,9 ,2 ,5 ,3 ,7 ,101 ,18]
r = Solution().lengthOfLIS(nums)
