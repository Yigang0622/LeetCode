# https://leetcode-cn.com/problems/summary-ranges/
# 汇总区间
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        ret = []
        while len(nums):
            group, nums = self.extract_group(nums, [])
            if len(group) == 1:
                ret.append(str(group[0]))
            else:
                ret.append('{}->{}'.format(group[0], group[-1]))
        return ret

    def extract_group(self, nums, current):
        if len(nums) == 0:
            return current, nums
        if len(current) and nums[0] - 1 != current[-1]:
            return current, nums
        p = nums[0]
        current.append(p)
        return self.extract_group(nums[1:], current)


r = Solution().summaryRanges([0, 1, 2, 4, 5, 7])
print(r)