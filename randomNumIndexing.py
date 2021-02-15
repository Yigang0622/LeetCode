from typing import List
import random


# 398. 随机数索引
# https://leetcode-cn.com/problems/random-pick-index/
# 蓄水池抽样

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans = -1
        k = 1
        for i, each in enumerate(self.nums):
            if each == target:
                rand = random.randint(1, k)
                if rand == 1:
                    # print('hit')
                    ans = i
                k += 1
        return ans


nums = [1, 2, 3, 3, 3]
# Your Solution object will be instantiated and called as such:
obj = Solution(nums)
param_1 = obj.pick(3)
print(param_1)
