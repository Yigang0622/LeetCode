# LeetCode
# splitIntoFibonacci 
# Created by Yigang Zhou on 2020/9/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 842. 将数组拆分成斐波那契序列
# https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence/
from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        self.ans = []
        self.solved = False
        self.search([],0,S)
        return self.ans

    def search(self, current, start, S):
        if self.solved:
            return

        n = len(S)
        if len(current) >= 3:
            if int(current[-1]) != int(current[-2]) + int(current[-3]):
                print(current, '无效')
                return

        if start == n:
            if len(current) >= 3:
                print(current)
                self.ans = current[:]
                self.solved = True
            return
        for i in range(start+1, n+1):
            s = S[start:i]
            if len(s) > 1 and s[0] == '0':
                continue
            if int(s) > 2 ** 31 - 1:
                continue
            current.append(s)
            self.search(current, i, S)
            current.pop()


S = "123456579"
r = Solution().splitIntoFibonacci(S)
print(r)