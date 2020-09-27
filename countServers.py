# LeetCode
# countServers 
# Created by Yigang Zhou on 2020/9/27.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 1267. 统计参与通信的服务器
# https://leetcode-cn.com/problems/count-servers-that-communicate/
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])

        


grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
r = Solution().countServers(grid)
