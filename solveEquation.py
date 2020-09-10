# LeetCode
# solveEquation 
# Created by Yigang Zhou on 2020/9/10.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 求解方程
# https://leetcode-cn.com/problems/solve-the-equation/

class Solution:
    def solveEquation(self, equation: str) -> str:
        arr = equation.split('=')
        left_total = arr[0]
        right_total = arr[1]
        num_x_l, num_l = self.extract(expression=left_total)
        num_x_r, num_r = self.extract(expression=right_total)

        num_x = num_x_l - num_x_r
        num = num_r - num_l
        if num_x == 0 and num == 0:
            return 'Infinite solutions'
        elif num_x == 0:
            return 'No solution'
        else:
            return 'x={}'.format(int(num/num_x))


    def extract(self, expression):
        num_x = 0
        num = 0

        temp = ''
        last_operand = ''
        for each in expression:
            if each == '+' or each == '-' and temp != '':
                n_x, n = self.check(last_operand+temp)
                num_x += n_x
                num += n
                last_operand = each
                temp = ''
            else:
                temp += each

        n_x, n = self.check(last_operand+temp)
        num_x += n_x
        num += n
        return num_x, num

    def check(self, segment):
        num_x = 0
        num = 0
        if segment[0] == '+': # +xx
            segment = segment[1:]
            if 'x' in segment:
                if segment == 'x':
                    num_x += 1
                else:
                    num_x += int(segment[:-1])
            else:
                num += int(segment)
        elif segment[0] == '-': # -xx
            segment = segment[1:]
            if 'x' in segment:
                if segment == 'x':
                    num_x -= 1
                else:
                    num_x -= int(segment[:-1])
            else:
                num -= int(segment)
        else: # xx
            if 'x' in segment:
                if segment == 'x':
                    num_x += 1
                else:
                    num_x += int(segment[:-1])
            else:
                num += int(segment)

        return num_x, num


equation = "x+5-3+x=6+x-2"
r = Solution().solveEquation(equation)
print(r)