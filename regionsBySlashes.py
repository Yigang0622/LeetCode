# LeetCode
# regionsBySlashes 
# Created by Yigang Zhou on 2020/10/8.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 959. 由斜杠划分区域
# https://leetcode-cn.com/problems/regions-cut-by-slashes/
from typing import List
import common.arrayCommon as array

class UnionFind:

    def __init__(self, cap):
        self.parents = [-1] * cap
        self.num_of_groups = cap

    def find(self,n):
        if self.parents[n] == -1:
            return n
        return self.find(self.parents[n])

    def union(self,n1,n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            # merge failed
            return -1
        else:
            self.num_of_groups -= 1
            # p1 as parent of p2
            self.parents[p2] = p1
            return p1

    # def print(self):
    #     print(self.parents)
    #     print(self.num_of_groups)

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        union_find = UnionFind(N*N*4)
        for i in range(N):
            for j in range(N):
                virtual_start = (i*N+j) * 4
                if grid[i][j] == '/':
                    union_find.union(virtual_start+1, virtual_start+2)
                    union_find.union(virtual_start+0, virtual_start+3)

                elif grid[i][j] == '\\':
                    union_find.union(virtual_start+0, virtual_start+1)
                    union_find.union(virtual_start+2, virtual_start+3)
                else:
                    union_find.union(virtual_start + 1, virtual_start + 0)
                    union_find.union(virtual_start + 2, virtual_start + 1)
                    union_find.union(virtual_start + 3, virtual_start + 2)
                # print(i,j)
                # 不是某行第一个
                if j != 0:
                    # print('union row')
                    union_find.union(virtual_start, virtual_start - 2)

                # 不是某列第一个
                if i != 0:
                    # print('union column')
                    union_find.union(virtual_start + 3, virtual_start - N * 4 + 1)
        # union_find.print()
        return union_find.num_of_groups



grid =[
  "//",
  "/ "
]
array.print2DArray(grid)
r = Solution().regionsBySlashes(grid)
print(r)