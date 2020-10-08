# LeetCode
# largestIsland 
# Created by Yigang Zhou on 2020/10/8.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 827. 最大人工岛
# https://leetcode-cn.com/problems/making-a-large-island/
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        parents = [-1] * (w * h)
        area = [0] * (w * h)
        visited = [[0] * w for _ in range(h)]
        ans = 0
        island_count = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    island_count += 1

                if grid[i][j] == 1 and visited[i][j] == 0:
                    parent = i * w + j
                    a = self.dfs(i, j, w, h, grid, visited, parents, parent)
                    # print(a)
                    area[parent] = a
        if island_count == w*h:
            return island_count

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0:
                    # c初始面积
                    a = 1
                    # 记录是否已经加过连通块
                    p_seen = set()
                    for i_next, j_next in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if i_next < 0 or i_next >= h or j_next < 0 or j_next >= w:
                            continue
                        if grid[i_next][j_next] == 1:
                            idx = i_next * w + j_next
                            if parents[idx] not in p_seen:
                                nei_area = area[parents[idx]]
                                # print(nei_area)
                                a += nei_area
                                p_seen.add(parents[idx])
                    ans = max(ans, a)
                    # print('ans', ans)
        return ans

    def dfs(self, i, j, w, h, grid, visited, parents, parent):
        if i < 0 or i >= h or j < 0 or j >= w:
            return 0
        if visited[i][j] == 1:
            return 0
        if grid[i][j] == 0:
            return 0
        count = 1
        visited[i][j] = 1
        parents[i * w + j] = parent
        for i_next, j_next in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            count += self.dfs(i_next, j_next, w, h, grid, visited, parents, parent)
        return count


grid = [[1, 1],
        [1, 0]]
print(grid)
r = Solution().largestIsland(grid=grid)
print(r)