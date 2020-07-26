# LeetCode
# merge 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
        return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

s = Solution().merge(nums1, 3, nums2, 3)
print(s)