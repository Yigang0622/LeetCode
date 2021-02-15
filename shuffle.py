from typing import List
import random
import copy
# 384. 打乱数组
# https://leetcode-cn.com/problems/shuffle-an-array/

class Solution:

    def swap(self, i, j):
        if i == j:
            return
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def __init__(self, nums: List[int]):
        self.original_nums = copy.deepcopy(nums)
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = copy.deepcopy(self.original_nums)
        return self.nums


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        l = len(self.nums)
        for i in range(l):
            rand = random.randint(i, l-1)
            self.swap(i, rand)
        return self.nums



# Your Solution object will be instantiated and called as such:
nums = [1,2,3,4,5,6,7,8,9]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_2)