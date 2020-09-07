# LeetCode
# findJudge 
# Created by Yigang Zhou on 2020/8/29.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# https://leetcode-cn.com/problems/find-the-town-judge/
# 找到小镇的法官
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        out_degree = [0] * N
        in_degree = [0] * N

        for each in trust:
            out_degree[each[0] - 1] += 1
            in_degree[each[1] - 1] += 1
        for i, each_out_degree in enumerate(out_degree):
            if each_out_degree == 0 and in_degree[i] == N - 1:
                return i + 1
        return -1


N = 4
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
r = Solution().findJudge(N, trust)
print(r)
