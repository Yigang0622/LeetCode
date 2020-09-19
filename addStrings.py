# LeetCode
# addStrings 
# Created by Yigang Zhou on 2020/9/19.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 字符串相加
# https://leetcode-cn.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == '0' and num2 == '0':
            return '0'
        if num1 == '0':
            return num2
        if num2 == '0':
            return num1
        n1 = len(num1)
        n2 = len(num2)
        if n1 < n2:
            return self.addStrings(num2, num1)
        delta = n1 - n2
        res = ''
        carry = 0
        for i in range(len(num1)- 1, -1, -1):
            num2_d = 0
            if i - delta >= 0:
                num2_d = num2[i-delta]
            temp = int(num1[i]) + int(num2_d) + carry
            carry = temp // 10
            res = str(temp % 10) + res
        if carry != 0:
            return str(carry) + res
        return res