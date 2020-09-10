# LeetCode
# checkStraightLine 
# Created by Yigang Zhou on 2020/9/9.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 缀点成线
# https://leetcode-cn.com/problems/check-if-it-is-a-straight-line/
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        k = 0
        denom = (coordinates[1][0] - coordinates[0][0])
        if denom != 0:
            k = (coordinates[1][1] - coordinates[0][1]) / denom

        N = len(coordinates)
        for i in range(2,N):
            k_i = 0
            d = (coordinates[i][0] - coordinates[1][0])
            if d != 0:
                k_i = (coordinates[i][1] - coordinates[1][1]) / d
            if k_i != k:
                return False
        return True

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
s = Solution().checkStraightLine(coordinates)
print(s)