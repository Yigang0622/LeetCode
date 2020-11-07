# LeetCode
# 74searchMatrix 
# Created by Yigang Zhou on 2020/11/7.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            return False

        h = len(matrix)
        w = len(matrix[0])

        l = 0
        r = w * h

        while l <= r:
            mid = (l + r) // 2
            i = mid // w
            j = mid % w
            if i >= h or j >= w:
                return False

            if matrix[i][j] > target:
                r = mid - 1
            elif matrix[i][j] < target:
                l = mid + 1
            else:
                return True

        return False


m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
target = 23
s = Solution().searchMatrix([[1]], target)
print(s)
