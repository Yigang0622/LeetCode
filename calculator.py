# LeetCode
# calculator 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# https://leetcode-cn.com/explore/interview/card/top-interview-questions/266/heap-stack-queue/1159/

class Solution:

    def calculate(self, s: str) -> int:
        print(s)
        elements = []
        suffix = []
        operands = []
        temp = ''
        # 转换
        for each in s:
            if each != ' ':
                if self.isOperand(each):
                    elements.append(temp)
                    temp = ''
                    elements.append(each)
                else:
                    temp += each
        if temp != '':
            elements.append(temp)
        print(elements)
        for each in elements:
            if self.isOperand(each):
                while len(operands) > 0 and self.compareOperand(each, operands[len(operands)-1]) is False:
                    suffix.append(operands[len(operands)-1])
                    operands.pop()
                operands.append(each)
            else:
                suffix.append(each)

        while len(operands) > 0:
            suffix.append(operands[len(operands) - 1])
            operands.pop()
        print(suffix)

        stack = []
        for each in suffix:
            if self.isOperand(each):
                ele1 = stack.pop()
                ele2 = stack.pop()
                result = self.cal(ele1, ele2, each)
                stack.append(result)
            else:
                stack.append(int(each))
        return stack[0]

    def cal(self, ele1, ele2, operand):
        if operand == '+':
            return ele1 + ele2
        elif operand == '-':
            return ele2 - ele1
        elif operand == '*':
            return ele1 * ele2
        elif operand == '/':
            return int(ele2 / ele1)

    def compareOperand(self, operand1, operand2):
        if (operand1 == '+' or operand1 == '-' ) and (operand2 == '*' or operand2 == '/'):
            return False
        elif (operand1 == '*' or operand1 == '/') and (operand2 == '+' or operand2 == '-' ):
            return True
        else:
            return False

    def isOperand(self, char):
        return char == '+' or char == '-' or char == '*' or char == '/'

r = Solution().calculate(" 3*2 + 4*5 ")
print(r)
