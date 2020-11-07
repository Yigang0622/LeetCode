# LeetCode
# search 
# Created by Yigang Zhou on 2020/11/7.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 33. 搜索旋转排序数组
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not len(nums):
            return -1
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[0] <= nums[mid]:
                    if nums[0] <= target < nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    if nums[mid] < target <= nums[-1]:
                        l = mid + 1
                    else:
                        r = mid - 1
        return -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
s = Solution().search(nums, target)
print(s)
