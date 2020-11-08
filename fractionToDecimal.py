
# LeetCode
# fractionToDecimal 
# Created by Yigang Zhou on 2020/11/8.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 166. 分数到小数
# https://leetcode-cn.com/problems/fraction-to-recurring-decimal/

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # print('{}/{}'.format(numerator, denominator))
        # 边界情况
        if denominator == 0:
            raise ZeroDivisionError("分母为0辣")

        if numerator == 0:
            return '0'

        result_is_negative = numerator * denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)

        # 整除情况
        if numerator % denominator == 0:
            res = str(numerator // denominator)
            if result_is_negative:
                return '-{}'.format(res)
            else:
                return '{}'.format(res)


        integer_part = '0'
        reminder = numerator
        if numerator > denominator:
            integer_part = str(numerator // denominator)
            reminder = numerator % denominator

        reminder *= 10
        # 储存余数出现的位置，如果产生循环节，那么一定会出现某个相同的余数
        d = dict()
        decimal = ''
        while reminder != 0:
            # 不够除的时候乘10
            # print('reminder:{}'.format(reminder))
            if reminder in d:
                decimal_period = decimal[d[reminder]:]
                # print('产生循环'+decimal_period)
                decimal = decimal[:d[reminder]] + '({})'.format(decimal_period)
                break
            d[reminder] = len(decimal)

            while reminder < denominator:
                # print('0!')
                decimal += '0'
                reminder = reminder * 10

            result = reminder // denominator
            decimal += str(result)
            reminder = reminder % denominator * 10
            # print(result)

        if result_is_negative:
            return '-{}.{}'.format(integer_part, decimal)
        else:
            return '{}.{}'.format(integer_part, decimal)




numerator = -4
denominator = -333
r = Solution().fractionToDecimal(numerator, denominator)
print(r)
