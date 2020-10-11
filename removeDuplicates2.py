# LeetCode
# removeDuplicates2 
# Created by Yigang Zhou on 2020/10/8.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 80. 删除排序数组中的重复项 II
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/
from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        i = 0
        for num in nums:
            # 第一位 第二位和第一位一样 第N位和第N-1位一样，但是和N-2位不一样
            if i == 0 or (i > 0 and nums[i-1] != num) or \
                    (i == 1 and nums[i - 1] == num) or\
                    (i > 1 and nums[i-1] == num and nums[i-2] != num):

                nums[i] = num
                i += 1
            else:
                nums[i] = num

        return i



nums = [0,0,1,1,1,1,2,3,3]
r = Solution().removeDuplicates(nums)
print(nums, r)