from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        eleStack = []
        for each in tokens:
            if self.isOperand(each):
                ele1 = eleStack.pop()
                ele2 = eleStack.pop()
                result = self.calculate(int(ele1), int(ele2), each)
                eleStack.append(result)
            else:
                eleStack.append(each)
        return int(eleStack.pop())

    def isOperand(self, token):
        return token == '+' or token == '-' or token == '*' or token == '/'

    def calculate(self, ele1, ele2, operand):
        if operand == '+':
            return ele1 + ele2
        elif operand == '-':
            return ele2 - ele1
        elif operand == '*':
            return ele1 * ele2
        elif operand == '/':
            return ele2 / ele1

s = Solution().evalRPN(["4","3","-"])

