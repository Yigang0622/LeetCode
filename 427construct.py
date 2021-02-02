# LeetCode
# 427construct 
# Created by Yigang Zhou on 2021/2/2.
# Copyright © 2021 Yigang Zhou. All rights reserved.

# 427. 建立四叉树
# https://leetcode-cn.com/problems/construct-quad-tree/

# Definition for a QuadTree node.
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:

    def checkSingleValue(self, grid, r1, c1, r2, c2):
        print(r1, c1, r2, c2)
        v = grid[r1][c1]
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if grid[i][j] != v:
                    # print('False')
                    return False
        return True

    def construct(self, grid: List[List[int]]) -> 'Node':
        # print(grid)
        N = len(grid)
        return self.helper(grid, 0,0, N-1, N-1)

    def helper(self, grid, r1, c1, r2, c2):
        # if r2 - r1 + 1 == 2:
        #     top_left = Node(grid[r1][c1], True, None, None, None, None)
        #     top_right = Node(grid[r1][c1+1], True, None, None, None, None)
        #     bottom_left = Node(grid[r2][c1], True, None, None, None, None)
        #     bottom_right = Node(grid[r2][c2], True, None, None, None, None)
        #     node = Node(1, False, top_left, top_right, bottom_left, bottom_right)
        #     return node
        # else:
        if self.checkSingleValue(grid, r1, c1,  r2, c2):
             return Node(grid[r1][c1], True, None, None, None, None)
        else:

            half_grid = int((r2 - r1 + 1) / 2)
            top_left = self.helper(grid, r1, c1, r1+half_grid-1, c1 + half_grid - 1)
            top_right = self.helper(grid, r1, c1 + half_grid, r1+half_grid-1, c2)
            bottom_left = self.helper(grid, r1 + half_grid, c1, r2, c1 + half_grid - 1)
            bottom_right = self.helper(grid, r1 + half_grid, c1 + half_grid, r2, c2)
            n = Node(grid[r1][c1], False, top_left, top_right, bottom_left, bottom_right)
            return n







grid =  [[0,1],[1,0]]
r = Solution().construct(grid)
a = 1