# LeetCode
# missingNumber 
# Created by Yigang Zhou on 2020/8/1.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnj4mt/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_expected = n*(n+1)//2
        actual_sum = sum(nums)
        return int(sum_expected-actual_sum)


r = Solution().missingNumber([3,0,1])
print(r)


