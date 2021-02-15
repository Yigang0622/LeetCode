# LeetCode
# calcEquation 
# Created by Yigang Zhou on 2021/1/30.
# Copyright © 2021 Yigang Zhou. All rights reserved.

# 399除法求值
# https://leetcode-cn.com/problems/evaluate-division/
from typing import List
import copy


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        s = set()
        for i, each in enumerate(equations):
            nominator = each[0]
            denominator = each[1]
            s.add(nominator)
            s.add(denominator)
            if nominator not in graph:
                graph[nominator] = {denominator: values[i]}
            else:
                graph[nominator][denominator] = values[i]

            if denominator not in graph:
                graph[denominator] = {nominator: 1.0 / values[i]}
            else:
                graph[denominator][nominator] = 1.0 / values[i]
        print(graph)
        ans = []
        for query in queries:
            nominator = query[0]
            denominator = query[1]

            if nominator not in s or denominator not in s:
                ans.append(-1)
            elif nominator == denominator:
                ans.append(1.0)
            else:
                r = self.solve(graph, nominator,denominator, [], [])
                ans.append(r)
        return ans

    def solve(self, graph, nominator, denominator, path, ratio):
        # print(path)
        if nominator == denominator:
            res = 1
            for each in ratio:
                res *= each
            return res

        if len(path) == 0:
            path.append(nominator)

        for each in graph[nominator]:
            if each not in path:
                p = copy.deepcopy(path)
                r = copy.deepcopy(ratio)
                p.append(each)
                r.append(graph[nominator][each])
                ans = self.solve(graph, each, denominator, p, r)
                if ans != -1:
                    return ans
                # path.pop()
                # ratio.pop()
        return -1





equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values =  [3.0,4.0,5.0,6.0]
queries =[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]

s = Solution()
r = s.calcEquation(equations, values, queries)
print(r)

