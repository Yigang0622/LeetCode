# LeetCode
# makeConnected 
# Created by Yigang Zhou on 2020/9/17.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 连通网络的操作次数
# https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected/
from typing import List


class Solution:

    def find_parent(self,p, parents):
        while parents[p] != -1:
            p = parents[p]
        return p



    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        n_edges = len(connections)
        if n_edges  < n - 1:
            return -1
        parents = [-1] * n

        number_of_redundent_edges = 0
        for edge in connections:
            f = edge[0]
            v = edge[1]
            p_f = self.find_parent(f,parents)
            p_v = self.find_parent(v,parents)
            if p_f == p_v:
                number_of_redundent_edges += 1
                # print(edge, '无意义')
            else:
                parents[p_f] = p_v

        # 需要的边数 n - 1
        # 当前有效的边数 = 边数 - 无效边数
        return (n - 1) - (n_edges - number_of_redundent_edges)




connections = [[0,1],[0,2],[1,2]]
n = 4
r = Solution().makeConnected(n, connections)
print(r)