# LeetCode
# isValidParentheses 
# Created by Yigang Zhou on 2020/8/1.
# Copyright © 2020 Yigang Zhou. All rights reserved.

class Solution:

    def isValid(self, s: str) -> bool:
        right = {')',']','}'}
        tokens = [x for x in s]
        stack = []

        if len(s) == 0:
            return True

        if len(s) %2 == 1:
            return False

        while len(tokens) > 0:
            t = tokens.pop()
            if t in right: #右括号
                stack.append(t)
            else: #左括号
                if len(stack) == 0:
                    return False
                else:
                    l = stack.pop()
                    print(t,l)
                    if (t is '(' and l is not ')') or (t is '{' and l is not '}') or (t is '[' and l is not ']'):
                        return False
        return True


s = Solution().isValid('(){}[]')
print(s)