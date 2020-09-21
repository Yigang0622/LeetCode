# 目标和
# https://leetcode-cn.com/leetbook/read/queue-stack/ga4o2/

from typing import List
import common.arrayCommon as Array


class Solution:

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        print(nums)
        s = sum(nums)
        if s < S:
            return 0

        n = len(nums)
        r = s * 2 + 1
        dp = [[0] * r for _ in range(n)]
        if nums[0] == 0:
            dp[0][s] = 2
        else:
            dp[0][s - nums[0]] = 1
            dp[0][s + nums[0]] = 1

        for i in range(1, n):
            for j in range(0, r):
                if j - nums[i] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i]]
                if j + nums[i] < r:
                    dp[i][j] += dp[i - 1][j + nums[i]]
        print(dp)
        return dp[-1][s + S]


nums = [0, 0, 0, 0, 0, 0, 0, 0, 1]
S = 1

r = Solution().findTargetSumWays(nums, S)
print(r)

# class Solution:
#     multiplier = [1, -1]
#     ans = 0
#
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         self.ans = 0
#         self.search(S, nums, 0, 0)
#         return self.ans
#
#     def search(self, target, nums, i, cur):
#         if i == len(nums):
#             if cur == target:
#                 self.ans += 1
#             return
#         for each in self.multiplier:
#             c = cur + each * nums[i]
#             self.search(target, nums, i + 1, c)
