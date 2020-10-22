# LeetCode
# backspaceCompare 
# Created by Yigang Zhou on 2020/10/19.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 844. 比较含退格的字符串
# https://leetcode-cn.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = self.simulate(S)
        t = self.simulate(T)
        # print(s, t)
        return s == t

    def simulate(self,S):
        arr = list(S)
        result = []
        for each in arr:
            if each == '#':
                if len(result):
                    result.pop()
            else:
                result.append(each)
        return result


S = "ab#c"
T = "ad#c"
s = Solution().backspaceCompare(S, T)
print(s)