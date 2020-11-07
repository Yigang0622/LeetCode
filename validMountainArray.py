# LeetCode
# validMountainArray 
# Created by Yigang Zhou on 2020/11/7.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 941. 有效的山脉数组
# https://leetcode-cn.com/problems/valid-mountain-array/
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) <= 1:
            return False
        # 0 up 1 down - 1 initial
        state = -1

        for i in range(1, len(A)):

           if A[i] > A[i-1]:
               if state == 1:
                   return False
               elif state == -1:
                   state = 0
           elif A[i] < A[i-1]:
               if state == 0:
                   state = 1
               elif state == -1:
                   return False
           else:
               return False
        return state == 1

A = [0, 2, 3, 4, 5, 2, 1, 0]
s = Solution().validMountainArray(A)
print(s)

