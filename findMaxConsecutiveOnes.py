# 最大连续1的个数
# https://leetcode-cn.com/leetbook/read/array-and-string/cd71t/
from typing import List


class Solution:
    
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        combo = 0
        max_consecutive = 0
        for each in nums:
            if each == 1:
                combo += 1
            else:
                max_consecutive = max(combo, max_consecutive)
                combo = 0
        max_consecutive = max(combo, max_consecutive)
        return max_consecutive


r = Solution().findMaxConsecutiveOnes([0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1])
print(r)
