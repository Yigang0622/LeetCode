# LeetCode
# judgePoint24 
# Created by Yigang Zhou on 2020/8/22.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 24 点
# https://leetcode-cn.com/problems/24-game/
from typing import List


class Solution:
    solvable = False
    e = 1e-6

    def judgePoint24(self, nums: List[int]) -> bool:
        self.solvable = False
        self.seach([],[], nums)
        return self.solvable

    def seach(self, cur,idx, nums):

        if self.solvable:
            return

        if len(cur) == 4:
            print(cur)
            if self.evaluate(cur):
                self.solvable = True
            return

        for i, each in enumerate(nums):
            if i not in idx:
                cur.append(each)
                idx.append(i)
                self.seach(cur, idx, nums)
                cur.pop()
                idx.pop()

    def evaluate(self, nums) -> bool:
        ops = ['+', '-', '*', '/']

        for i in ops:
            for j in ops:
                for k in ops:
                    if i == '/' and nums[1] == 0:
                        break

                    r1 = self.eval(nums[0], nums[1], i)

                    if j == '/' and nums[2] == 0:
                        break
                    r2 = self.eval(r1, nums[2], i)

                    if k == '/' and nums[3] == 0:
                        break
                    result = self.eval(r2, nums[3], k)
                    if abs(result - 24) < self.e:
                        print('!!!!!', i, k, j, nums)
                        return True

        return False

    def eval(self, e1, e2, op):
        if op == '+':
            return e1 + e2
        if op == '-':
            return e1 - e2
        if op == '*':
            return e1 * e2
        if op == '/':
            return e1 / e2


nums = [3,9,7,7]
r = Solution().judgePoint24(nums)
print(r)
