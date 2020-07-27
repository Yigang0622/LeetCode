# https://leetcode-cn.com/explore/interview/card/top-interview-questions/264/array/1126/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        print(nums)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        pd = [0] * len(nums)
        pd[0] = nums[0]
        max_product = nums[0]
        for i in range(1, len(nums)):
            pd[i] = max(pd[i-1]*nums[i], nums[i])
            if pd[i] > max_product:
                max_product = pd[i]
        print(pd)
        return max(pd)


Solution().maxProduct([-2,3,-4])