# 寻找数组的中心索引
# https://leetcode-cn.com/leetbook/read/array-and-string/yf47s/
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return -1
        l = 0
        r = n - 1
        left_sum = nums[l]
        right_sum = nums[r]
        while l<r:
            if left_sum < right_sum:
                l += 1
                left_sum += nums[l]
            else:
                r -= 1
                right_sum += nums[r]
        print(left_sum, right_sum, l, r)

        if left_sum == right_sum:
            return l
        else:
            return -1



r = Solution().pivotIndex([1,7,3,6,5,6])
print(r)