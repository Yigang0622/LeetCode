from typing import List
from common.arrayCommon import *

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/51/dynamic-programming/104/

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        right_most_pos = 0
        for i, step in enumerate(nums):
            max_pos = max(right_most_pos, i + step)
            if right_most_pos >= i and max_pos > right_most_pos:
                right_most_pos = max_pos
        return right_most_pos >= len(nums) - 1


arr = [0, 1]
r = Solution().canJump(arr)
print(r)
