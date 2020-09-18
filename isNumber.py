# LeetCode
# isNumber 
# Created by Yigang Zhou on 2020/9/16.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 剑指 Offer 20. 表示数值的字符串
# https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/
# +100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
# 但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。


class Solution:
    def isNumber(self, s: str) -> bool:

        STATE_INITIAL_SIGN = 1  # 开始的符号
        STATE_INTEGER_PART = 2  # 整数部分
        STATE_DECIMAL_POINT_WITH_INTEGER_PART = 3  # 整数后的小数点
        STATE_DECIMAL_POINT_WITHOUT_INTEGER_PART = 4  # 没有整数的小数点
        STATE_DECIMAL_PART = 5  # 小数部分
        STATE_E = 6  # E/e
        STATE_E_SIGN = 7  # E后面的符号 +/-
        STATE_E_INTEGER = 8  # E后的整数部分

        last_state = -1 #起始状态
        s = s.strip()
        if s == '.':
            return False
        for each in s:
            if each == '+' or each == '-':
                if last_state == -1:
                    last_state = STATE_INITIAL_SIGN
                elif last_state == STATE_E:
                    last_state = STATE_E_SIGN
                else:
                    return False
            elif each == '.':
                if last_state == STATE_INITIAL_SIGN or last_state == -1:
                    last_state = STATE_DECIMAL_POINT_WITHOUT_INTEGER_PART
                elif last_state == STATE_INTEGER_PART:
                    last_state = STATE_DECIMAL_POINT_WITH_INTEGER_PART
                else:
                    return False
            elif each == 'e' or each == 'E':
                if last_state == STATE_INTEGER_PART or last_state == STATE_DECIMAL_PART or last_state == STATE_DECIMAL_POINT_WITH_INTEGER_PART:
                    last_state = STATE_E
                else:
                    return False
            else:
                if each.isdigit():
                    if last_state == STATE_E_SIGN:
                        last_state = STATE_E_INTEGER
                    elif last_state == STATE_INITIAL_SIGN:
                        last_state = STATE_INTEGER_PART
                    elif last_state == STATE_DECIMAL_POINT_WITH_INTEGER_PART \
                            or last_state == STATE_DECIMAL_POINT_WITHOUT_INTEGER_PART:
                        last_state = STATE_DECIMAL_PART
                    elif last_state == STATE_E:
                        last_state = STATE_E_INTEGER
                    elif last_state == STATE_E_SIGN:
                        last_state = STATE_E_INTEGER
                    elif last_state == -1:
                        last_state = STATE_INTEGER_PART
                else:
                    return False
            # print(last_state)
        return last_state == STATE_INTEGER_PART or last_state == STATE_DECIMAL_PART or last_state == STATE_E_INTEGER or last_state == STATE_DECIMAL_POINT_WITH_INTEGER_PART

s = Solution().isNumber('5.')
print(s)