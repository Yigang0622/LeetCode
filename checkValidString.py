# LeetCode
# checkValidString 
# Created by Yigang Zhou on 2020/9/19.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 有效的括号字符串
# https://leetcode-cn.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        # 可能多余的左括号数目的上界和下届
        low = 0
        high = 0

        for each in s:
            if each == '(':
                low += 1
                high += 1
            elif each == '*':
                if low > 0:
                    low -= 1
                high += 1
            elif each == ')':
                if low > 0:
                    low -= 1
                high -= 1

            if high < 0:
                return False
        return low == 0

s = "(*))"
r = Solution().checkValidString(s)
print(r)