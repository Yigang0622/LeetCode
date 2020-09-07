# 前k个高频元素
# https://leetcode-cn.com/problems/top-k-frequent-elements/
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print(nums)

nums = [1,1,1,2,2,3]
k = 2
r = Solution().topKFrequent(nums, k)