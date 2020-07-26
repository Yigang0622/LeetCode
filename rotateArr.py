# LeetCode
# rotateArr 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# https://leetcode-cn.com/explore/interview/card/top-interview-questions/264/array/1128/
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:
            return
        if len(nums) < k:
            k = k % len(nums)

        if len(nums) == k:
            return

        temp_arr = []
        length = len(nums)
        for i in range(length - k, length):
            temp_arr.append(nums[i])

        for i in range(length-k):
            nums[length - i - 1] = nums[length - i - k - 1]

        for i in range(k):
            nums[i] = temp_arr[i]
        print(nums)

r= Solution().rotate([1,2],3)