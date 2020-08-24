# LeetCode
# intToRoman 
# Created by Yigang Zhou on 2020/8/23.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# https://leetcode-cn.com/problems/integer-to-roman/
# 整数转罗马数字

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_digits = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ''
        while num > 0:
            for i, each in enumerate(integers):
                if each <= num: # 贪心
                    roman += roman_digits[i]
                    num -= each
                    break
        return roman

num = 432
s = Solution().intToRoman(num)
print(s)

