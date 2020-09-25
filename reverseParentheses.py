
# 1190. 反转每对括号间的子串
# https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/
import collections

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for each in s:
            if each == ')':
                q = collections.deque()
                while stack[-1] != '(':
                    q.append(stack.pop())
                stack.pop() # pop左括号
                while q:
                    stack.append(q.popleft())
            else:
                stack.append(each)
        # print(stack)
        return ''.join(stack)



s = "a(bcdefghijkl(mno)p)q"
r = Solution().reverseParentheses(s)
print(r)