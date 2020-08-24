# LeetCode
# canFinish 
# Created by Yigang Zhou on 2020/8/22.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List

# 课程表
# https://leetcode-cn.com/problems/course-schedule/


class Solution:

    graph_valid = True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for _ in range(numCourses)]
        # 0未搜索 1搜索中 2已搜索
        visited = [0] * numCourses
        ans = []
        for each in prerequisites:
            edges[each[1]].append(each[0])

        for course in range(numCourses):
            if self.graph_valid and visited[course] == 0:
                self.dfs(edges, visited, course, ans)
        return self.graph_valid

    def dfs(self, edges, visited, course, ans):

        visited[course] = 1

        for each_edge in edges[course]:

            if visited[each_edge] == 1:
                self.graph_valid = False
                return
            if visited[each_edge] == 0:
                self.dfs(edges, visited,each_edge,ans)
                if not self.graph_valid:
                    return

        visited[course] = 2
        ans.append(course)

numCourses = 9
prerequisites = [[2, 0], [2, 1], [3, 2], [3, 4], [4, 1], [5, 3], [5, 4], [6, 3], [6, 8], [7, 0], [8, 7]]
r = Solution().canFinish(4, [[1,0],[2,0],[3,1],[3,2]])