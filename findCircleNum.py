# https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdxc56/
# 朋友圈
from typing import List
import common.arrayCommon as Array


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        if n == 0:
            return 0
        count = 0
        visited = [False for _ in range(n)]
        for i in range(n):
            if not visited[i]:
                # Search
                self.search(M, visited, i)
                count += 1
                # print(i)
                # print(visited)

        return count

    def search(self, M, visited, i):
        n = len(M)
        for j in range(n):
            if not visited[j] and M[i][j] == 1:  # 是朋友
                visited[j] = True
                self.search(M, visited, j)  # 找j的朋友


M = [[1, 1, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 0],
     [0, 0, 1, 1, 0, 0],
     [0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 1]]
Array.print2DArray(M)
r = Solution().findCircleNum(M)
print(r)
