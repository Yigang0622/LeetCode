from typing import List

# 684 冗余链接
# https://leetcode-cn.com/problems/redundant-connection/


class UnionFind:

    def __init__(self, n):
        self.parent = [-1] * (n + 1)

    def find(self, u):
        if self.parent[u] == -1:
            return u
        return self.find(self.parent[u])

    def union(self, u1, u2):
        p1 = self.find(u1)
        p2 = self.find(u2)

        if p1 == p2: # union failed
            return -1
        else:
            self.parent[p1] = p2
            return u2

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind(len(edges))
        for each in edges:
            if union_find.union(each[0], each[1]) == -1:
                return each



edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
s = Solution().findRedundantConnection(edges)
print(s)