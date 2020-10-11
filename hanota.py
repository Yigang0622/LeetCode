# LeetCode
# hanota 
# Created by Yigang Zhou on 2020/10/9.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        self.move(n, A, B, C)

    # move n plates from A to C through B
    def move(self, n, A, B, C):
        if n == 1:
            e = A.pop()
            C.append(e)
        else:
            self.move(n-1, A, C, B)
            e = A.pop()
            C.append(e)
            self.move(n-1, B, A, C)

A = [2, 1, 0]
B = []
C = []
r = Solution().hanota(A,B,C)