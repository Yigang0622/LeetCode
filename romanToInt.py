# LeetCode
# romanToInt 
# Created by Yigang Zhou on 2020/8/1.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn4n7c/

# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:

    def romanToInt(self, s: str) -> int:
        sum = 0
        pirority = ['M','D','C','L','X','V','I']
        arr = [x for x in s]
        last = ''
        while len(arr):
            e = arr.pop()
            if last == '':
                sum += self.charToInt(e)
            else:
                if pirority.index(last) >= pirority.index(e):
                    sum += self.charToInt(e)
                else:
                    sum -= self.charToInt(e)

            last = e

        return sum

    def charToInt(self, char):
        if char == 'I':
            return 1
        elif char == 'V':
            return 5
        elif char == 'X':
            return 10
        elif char == 'L':
            return 50
        elif char == 'C':
            return 100
        elif char == 'D':
            return 500
        elif char == 'M':
            return 1000

r = Solution().romanToInt('MCMXCIV')
print(r)