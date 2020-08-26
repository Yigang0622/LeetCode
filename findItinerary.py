# LeetCode
# findItinerary 
# Created by Yigang Zhou on 2020/8/27.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 重新安排行程
# https://leetcode-cn.com/problems/reconstruct-itinerary/
from typing import List
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = {}
        for each in tickets:
            start = each[0]
            if start in edges:
                heapq.heappush(edges[start], each[1])
            else:
                edges[start] = [each[1]]
        path = ['JFK']
        visited = set()
        self.dfs(edges,'JFK',visited,path)
        return path

    def dfs(self, edges, airport,visited, path):
        if airport not in edges:
            return
        dests = heapq.nlargest(len(edges[airport]),edges[airport])
        for destination in dests:
            p = airport + destination
            if p not in visited:
                visited.add(p)
                path.append(destination)
                self.dfs(edges, destination, visited, path)



tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
r = Solution().findItinerary(tickets)
print(r)