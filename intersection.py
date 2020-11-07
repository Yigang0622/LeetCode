# LeetCode
# intersection 
# Created by Yigang Zhou on 2020/11/2.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 349. 两个数组的交集
# https://leetcode-cn.com/problems/intersection-of-two-arrays/
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        ans = []
        if len(s2) > len(s1):
            for each in s1:
                if each in s2:
                    ans.append(each)
        else:
            for each in s2:
                if each in s1:
                    ans.append(each)

        return ans



nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
s = Solution().intersection(nums1, nums2)
print(s)