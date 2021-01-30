# LeetCode
# shortestPathBinaryMatrix 
# Created by Yigang Zhou on 2021/1/30.
# Copyright © 2021 Yigang Zhou. All rights reserved.

# 1091. 二进制矩阵中的最短路径
# https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/
from typing import List
import collections

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # print(grid)
        N = len(grid)
        if N == 1:
            return 1
        if grid[N-1][N-1] == 1:
            return -1
        if grid[0][0] == 1:
            return -1

        seen = set()
        seen.add((0,0))
        q = collections.deque()
        q.append((0,0))

        steps = 1
        while q:
            steps += 1
            for x in range(len(q)):
                i,j = q.popleft()
                moves = self.possibleNextMoves(grid, N, seen, i, j)
                # print(moves)
                for i_next, j_next in moves:
                    if i_next == N -1 and j_next == N - 1:
                        return steps
                    next_move = (i_next, j_next)
                    seen.add(next_move)
                    q.append(next_move)
        return -1

    def possibleNextMoves(self, grid, N,  seen, i, j):
        res = []
        for i_next in range(i - 1, i + 2):
            for j_next in range(j - 1, j + 2):
                if 0 <= i_next < N and 0 <= j_next < N:
                    if (i_next, j_next) not in seen:
                        if grid[i_next][j_next] == 0:
                            res.append((i_next, j_next))
        return res




grid = [[0,1],[1,0]]
r = Solution().shortestPathBinaryMatrix(grid)
print(r)