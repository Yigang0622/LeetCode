# LeetCode
# kthSmallest 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List
import collections

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix) == 0:
            return 0

        n = len(matrix)
        i = int((k - 1)/n)
        j = (k-1)%n
        print(i,j)
        print(matrix[i][j])
        return matrix[i][j]



matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
s = Solution().kthSmallest(matrix,k)