# LeetCode
# largestNumber 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(x) for x in nums]
        nums_str.sort(reverse=True)
        s = ''
        for each in nums_str:
            s += each
        return s




r = Solution().largestNumber([3,30,34,5,9])