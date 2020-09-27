# LeetCode
# eventualSafeNodes 
# Created by Yigang Zhou on 2020/9/27.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        n = len(graph)
        # 0 没有访问 1访问中 2访问过了并且没有环
        state = [0] * n
        print(state)
        for i in range(n):
            if self.dfs(i, state, graph):
                ans.append(i)
        print(state)
        print(ans)
        return ans


    def dfs(self, node, state, graph):
        if state[node] == 1:
            return False
        if state[node] == 2:
            return True

        state[node] = 1
        for neighbour in graph[node]:
            if state[neighbour] == 2:
                continue
            if state[neighbour] == 1:
                return False
            if not self.dfs(neighbour, state, graph):
                return False
        state[node] = 2
        return True





graph = [[1,2],[2,3],[5],[0],[5],[],[]]
r = Solution().eventualSafeNodes(graph)

