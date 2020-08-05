# https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xw6oqi/
# 盛水最多的容器
# 双指针
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


r = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
