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

'VI'

class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
            '': 0,
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sum = 0
        last_chr = ''

        while len(s):
            element = s[-1]
            if dictionary[last_chr] <= dictionary[element]:
                sum += dictionary[element]
            else:
                sum -= dictionary[element]
            last_chr = element
            s = s[:-1]
        return sum


s = Solution()
result = s.romanToInt('III')
print(result)
