# LeetCode
# equationsPossible 
# Created by Yigang Zhou on 2020/9/19.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 990. 等式方程的可满足性
# https://leetcode-cn.com/problems/satisfiability-of-equality-equations/
from typing import List


class UnionFind:

    def __init__(self):
        self.parent = [-1] * 26

    def find_parent(self, n):
        if self.parent[n] == -1:
            return n
        return self.find_parent(self.parent[n])

    def union(self, n1, n2):
        p_1 = self.find_parent(n1)
        p_2 = self.find_parent(n2)
        if p_1 == p_2:
            return -1
        else:
            self.parent[p_1] = p_2
            return p_2


class Solution:

    def equationsPossible(self, equations: List[str]) -> bool:
        unionFind = UnionFind()

        # 排序 == 先 ！= 后
        equations_sorted = [x for x in equations if x[1:3] == '=='] + [x for x in equations if x[1:3] == '!=']
        # print(equations_sorted)
        for each in equations_sorted:
            e1 = each[0]
            e2 = each[3]
            equality = each[1:3]
            # print('->', e1, equality, e2)
            e1_num = ord(e1) - 97
            e2_num = ord(e2) - 97
            if equality == '==':
                unionFind.union(e1_num, e2_num)

            if equality == '!=':
                p1 = unionFind.find_parent(e1_num)
                p2 = unionFind.find_parent(e2_num)
                if p1 == p2:
                    # print('p1 == p2')
                    return False

        return True


equations = ["a==b","b!=c","c==a"]
r = Solution().equationsPossible(equations)
print(r)
