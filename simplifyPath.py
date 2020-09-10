# LeetCode
# simplifyPath 
# Created by Yigang Zhou on 2020/9/9.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 简化路径
# https://leetcode-cn.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        arr = [x for x in path.split('/') if x != '']
        for each in arr:
            if each == '..':
                if s:
                    s.pop()
            elif each == '.':
                pass
            else:
                s.append(each)
        if not s:
            return '/'

        return "/" + "/".join(s)



path = '/a/../../b/../c//.//'
r = Solution().simplifyPath(path)
print(r)


