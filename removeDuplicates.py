# 删除排序数组中的重复项
# https://leetcode-cn.com/leetbook/read/array-and-string/cq376/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        cur = 0
        for i in range(n):
            if nums[cur] != nums[i]:
                cur += 1
            nums[cur] = nums[i]
        return cur + 1

r = Solution().removeDuplicates([1,1,2])
print(r)