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
import collections


class Solution:

    def romanToInt(self, s: str) -> int:
        sum = 0

        priority = {
            'I': 6,
            'V': 5,
            'X': 4,
            'L': 3,
            'C': 2,
            'D': 1,
            'M': 0
        }

        dictionary = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        arr = [x for x in s]
        last = ''
        while len(arr):
            # 取每一位
            e = arr.pop()
            if last == '':  # 如果是第一位，直接加
                sum += dictionary[e]
            else:
                # 否则和上一位进行优先级比较
                if priority[last] >= priority[e]:
                    sum += dictionary[e]
                else:
                    sum -= dictionary[e]

            last = e

        return sum


r = Solution().romanToInt('MCMXCV')
print(r)
