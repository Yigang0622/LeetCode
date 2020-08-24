# LeetCode
# findOrder 
# Created by Yigang Zhou on 2020/8/22.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 课程表II
# https://leetcode-cn.com/problems/course-schedule-ii/
from typing import List


class Solution:

    graph_valid = True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = [[] for _ in range(numCourses)]
        # 0未搜索 1搜索中 2已搜索
        visited = [0] * numCourses
        ans = []
        for each in prerequisites:
            edges[each[1]].append(each[0])

        for course in range(numCourses):
            if self.graph_valid and visited[course] == 0:
                self.dfs(edges, visited, course, ans)
                
        if self.graph_valid:
            return ans[::-1]
        else:
            return []

    def dfs(self, edges, visited, course, ans):

        visited[course] = 1

        for each_edge in edges[course]:

            if visited[each_edge] == 1:
                self.graph_valid = False
                return
            if visited[each_edge] == 0:
                self.dfs(edges, visited, each_edge, ans)
                if not self.graph_valid:
                    return

        visited[course] = 2
        ans.append(course)