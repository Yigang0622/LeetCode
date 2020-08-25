# LeetCode
# pondSizes 
# Created by Yigang Zhou on 2020/8/25.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 岛屿大小
# https://leetcode-cn.com/problems/pond-sizes-lcci/
from typing import List
import common.arrayCommon as Array
import heapq


class Solution:

    def pondSizes(self, land: List[List[int]]) -> List[int]:

        h = len(land)
        w = len(land[0])
        result = []
        for i in range(h):
            for j in range(w):
                if land[i][j] == 0:
                    a = []
                    self.search(land, w, h, i, j, a)
                    heapq.heappush(result, len(a))
        return heapq.nsmallest(len(result), result)

    def search(self, land, w, h, i, j, ans):
        if i < 0 or i >= h or j < 0 or j >= w:
            return
        if land[i][j] != 0:
            return
        if land[i][j] == 0:
            land[i][j] = 1
            ans.append(0)
            self.search(land, w, h, i + 1, j + 1, ans)
            self.search(land, w, h, i - 1, j - 1, ans)
            self.search(land, w, h, i + 1, j - 1, ans)
            self.search(land, w, h, i - 1, j + 1, ans)
            self.search(land, w, h, i - 1, j, ans)
            self.search(land, w, h, i + 1, j, ans)
            self.search(land, w, h, i, j + 1, ans)
            self.search(land, w, h, i, j - 1, ans)


land = [
    [0, 2, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1]
]
Array.print2DArray(land)
r = Solution().pondSizes(land)
print(r)
