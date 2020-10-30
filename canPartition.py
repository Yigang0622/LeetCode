from typing import List
import common.arrayCommon as array
# 416. 分割等和子集
# https://leetcode-cn.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        sum_of_nums = sum(nums)
        max_of_nums = max(nums)
        if sum_of_nums % 2 != 0:
            return False

        target = sum_of_nums // 2
        if max_of_nums > target:
            return False

        dp = [[0] * (int(target)+1) for _ in range(len(nums))]

        for each in dp:
            each[0] = 1

        dp[0][nums[0]] = 1

        for i in range(1, len(nums)):
            for j in range(1, int(target)+1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i]]


        array.print2DArray(dp)
        return dp[-1][-1] == 1


nums = [1,5,11,5]
s = Solution().canPartition(nums)
print(s)