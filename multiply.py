# LeetCode
# multiply 
# Created by Yigang Zhou on 2020/9/19.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 字符串相乘
# https://leetcode-cn.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        if len(num1) < len(num2):
            return self.multiply(num2, num1)
        n1 = len(num1)
        n2 = len(num2)
        if n1 < n2:
            return self.multiply(num2, num1)
        res = ''

        for i in range(len(num2) - 1, -1, -1):
            offset = n2 - i - 1
            line = self.multiplyByDigit(num1,num2[i],offset)
            res = self.add(res, line)
        return res

    def add(self, num1, num2):
        if num1 == '0' and num2 == '0':
            return '0'
        if num1 == '0':
            return num2
        if num2 == '0':
            return num1
        n1 = len(num1)
        n2 = len(num2)
        if n1 < n2:
            return self.add(num2, num1)
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

    # 12345 * 1 或者 12345 * 7，只乘1位
    def multiplyByDigit(self, num, digit,offset):
        res = '0' * offset

        carry = 0
        for i in range(len(num) - 1, -1, -1):
            temp = int(num[i]) * int(digit) + carry
            carry = temp // 10
            res = str(temp % 10) + res
        if carry != 0:
            return str(carry) + res
        return res





num1 = '9999'
num2 = '101'
r  = Solution().multiply(num1, num2)
print(r)