# LeetCode
# minRemoveToMakeValid 
# Created by Yigang Zhou on 2020/9/28.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 1249. 移除无效的括号
# https://leetcode-cn.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_be_removed_index = set()
        stack = []
        for i, each in enumerate(s):
            if each == '(':
                stack.append(i)
            elif each == ')':
                if len(stack):
                    stack.pop()
                else:
                    to_be_removed_index.add(i)
        while stack:
            to_be_removed_index.add(stack.pop())
        res = []
        for i, each in enumerate(s):
            if i not in to_be_removed_index:
                res.append(each)
        return ''.join(res)


s = "lee(t(c)o)de))"
r = Solution().minRemoveToMakeValid(s)
print(r)