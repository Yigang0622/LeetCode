# LeetCode
# twoSum 
# Created by Yigang Zhou on 2020/10/1.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List

# https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
# 167. 两数之和 II - 输入有序数组

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) -1
        while i<j:
            s = numbers[i] + numbers[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return [i+1, j+1]
        return []


numbers = [2, 7, 11, 15]
target = 18
r = Solution().twoSum(numbers, target)
print(r)


