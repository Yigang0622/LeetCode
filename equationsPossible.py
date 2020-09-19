# LeetCode
# equationsPossible 
# Created by Yigang Zhou on 2020/9/19.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 990. 等式方程的可满足性
# https://leetcode-cn.com/problems/satisfiability-of-equality-equations/
from typing import List


class Solution:

    def equationsPossible(self, equations: List[str]) -> bool:
        self.val_dict = dict()
        self.val_count = 0

        for each in equations:
            print(self.val_dict)
            e1 = each[0]
            e2 = each[3]
            equality = each[1:3]
            print('->',e1,equality,e2)
            if equality == '==':

                if e1 not in self.val_dict and e2 not in self.val_dict:
                    self.assignSameValue(e1, e2)
                if e1 not in self.val_dict:
                    self.val_dict[e1] = self.val_dict[e2]
                if e2 not in self.val_dict:
                    self.val_dict[e2] = self.val_dict[e1]
                if e1 in self.val_dict and e2 in self.val_dict:
                    if self.val_dict[e1] != self.val_dict[e2]:
                        return False

            if equality == '!=':
                if e1 not in self.val_dict and e2 not in self.val_dict:
                    if e1 != e2:
                        self.assignDifferentValue(e1)
                        self.assignDifferentValue(e2)
                    else:
                        self.assignDifferentValue(e1)

                if e1 not in self.val_dict:
                    self.assignDifferentValue(e1)
                if e2 not in self.val_dict:
                    self.assignDifferentValue(e2)
                if e1 in self.val_dict and e2 in self.val_dict:
                    if self.val_dict[e1] == self.val_dict[e2]:
                        return False

        return True

    def assignSameValue(self,k1,k2):
        self.val_dict[k1] = self.val_count
        self.val_dict[k2] = self.val_count
        print(k1,'set to', self.val_count)
        print(k2,'set to', self.val_count)
        self.val_count += 1

    def assignDifferentValue(self, k):
        if k in self.val_dict:
            print(k,self.val_dict[k])
            return self.val_dict[k]
        print(k,'set to', self.val_count)
        self.val_dict[k] = self.val_count
        self.val_count += 1

equations = ["c==c","f!=a","f==b","b==c"]
r = Solution().equationsPossible(equations)
print(r)