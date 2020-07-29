# LeetCode
# longestCommonPrefix 
# Created by Yigang Zhou on 2020/7/21.
# Copyright © 2020 Yigang Zhou. All rights reserved.

#   最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]

        if len(strs) < 2:
            return ""
        max_len = len(strs[0])
        for each in strs:
            if len(each) < max_len:
                max_len = len(each)
        r = ''
        for i in range(max_len):
            c = strs[0][i]
            for each in strs:
                if each[i] != c:
                    c = ''
            if c == '':
                return r
            r += c

        return r


r = Solution().longestCommonPrefix(["flower","flow","flight"])
print(r)