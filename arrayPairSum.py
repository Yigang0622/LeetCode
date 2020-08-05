# 数组拆分I
# https://leetcode-cn.com/leetbook/read/array-and-string/c24he/
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        i = 0
        n = len(nums) - 1
        while i < n:
            sum += nums[i]
            i += 2
        return sum

r = Solution().arrayPairSum([])