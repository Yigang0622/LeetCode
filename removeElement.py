# 移除元素
# https://leetcode-cn.com/leetbook/read/array-and-string/cwuyj/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        cur = 0
        for i in range(n):
            nums[cur] = nums[i]
            if nums[i] != val:
                cur += 1
        return cur

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
r = Solution().removeElement(nums, val)