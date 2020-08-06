# 寻找旋转排序数组中的最小值
# https://leetcode-cn.com/leetbook/read/array-and-string/c3ki5/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]

r = Solution().findMin([1,2,3,4,5,6,0])
print(r)
