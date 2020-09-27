# LeetCode
# shortestBridge 
# Created by Yigang Zhou on 2020/9/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List
import collections


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        h = len(A)
        w = len(A[0])
        visited = set()
        q = collections.deque()
        min_dist = float('inf')

        should_dfs = True
        for i in range(h):
            if not should_dfs:
                break
            for j in range(w):
                if not should_dfs:
                    break
                if A[i][j] == 1 and should_dfs:
                    self.dfs(i, j, A, w, h, visited, q)
                    should_dfs = False
        while q:
            i, j, dist = q.popleft()

            if A[i][j] == 1 and dist != 0:
                # print('dist', dist - 1)
                min_dist = min(min_dist, dist - 1)
                # 跳出while，因为之后遍历到的点肯定没有这个近
                break

            for i_next, j_next in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= i_next < h and 0 <= j_next < w and (i_next, j_next) not in visited:
                    # print('!!!', i_next, j_next)
                    visited.add((i_next, j_next))
                    q.append((i_next,j_next,dist+1))
        return min_dist


    def dfs(self, i, j, A, w, h, visited, q):
        if i < 0 or i >= h or j < 0 or j >= w:
            return
        if (i, j) in visited:
            return
        if A[i][j] == 0:
            return
        # print('ADD', i, j)
        visited.add((i, j))
        q.append((i, j, 0))
        for i_next, j_next in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            self.dfs(i_next, j_next, A, w, h, visited, q)


A = [[0,1,0],[0,0,0],[0,0,1]]
r = Solution().shortestBridge(A)
print(r)
