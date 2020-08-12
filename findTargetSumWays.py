# 目标和
# https://leetcode-cn.com/leetbook/read/queue-stack/ga4o2/

from typing import List


class Solution:
    multiplier = [1, -1]
    ans = 0

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.ans = 0
        self.search(S, nums, 0, 0)
        return self.ans

    def search(self, target, nums, i, cur):
        if i == len(nums):
            if cur == target:
                self.ans += 1
            return
        for each in self.multiplier:
            c = cur + each * nums[i]
            self.search(target, nums, i + 1, c)


nums = [7, 46, 36, 49, 5, 34, 25, 39, 41, 38, 49, 47, 17, 11, 1, 41, 7, 16, 23, 13]
S = 3

r = Solution().findTargetSumWays(nums, 3)
print(r)
