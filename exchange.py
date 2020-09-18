# LeetCode
# exchange 
# Created by Yigang Zhou on 2020/9/16.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
# https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            while nums[i] % 2 == 1 and i < j:
                i += 1
            while nums[j] % 2 == 0 and i < j:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums



r = Solution().exchange([1,3,5])
print(r)