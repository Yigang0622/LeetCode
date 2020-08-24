# LeetCode
# networkDelayTime 
# Created by Yigang Zhou on 2020/8/23.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 网络延迟时间
# https://leetcode-cn.com/problems/network-delay-time/
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = [[] for _ in range(N)]
        for each in times:
            g[each[0] - 1].append((each[1] - 1, each[2]))
        delay = [float('inf') for _ in range(N)]
        self.dfs(delay, g, K - 1, 0)
        print(delay)
        if float('inf') in delay:
            return -1
        else:
            return int(max(delay))

    def dfs(self, delay, g, k, time_elapsed):
        # 当前延迟比最优延迟大，放弃搜索
        if time_elapsed > delay[k]:
            return
        delay[k] = time_elapsed
        for next, time in g[k]:
            self.dfs(delay, g, next, time_elapsed + time)


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1], [3, 5, 9000]]
N = 5
K = 2

s = Solution().networkDelayTime(times, N, K)
print(s)
