# LeetCode
# first_unique_char
# Created by Yigang Zhou on 2020/7/21.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 - 1。
#
# 示例：
# s = "leetcode"
# 返回
# 0
# s = "loveleetcode"
# 返回
# 2
# 提示：你可以假定该字符串只包含小写字母。

class Solution(object):

    occurrence = [0] * 26
    exist = [-1] * 26

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int

        """
        if len(s) == 0:
            return -1

        for i in range(len(s)):
            self.occurrence[self.char_to_index(s[i])] += 1
            if self.exist[self.char_to_index(s[i])] == -1:
                self.exist[self.char_to_index(s[i])] = i

        temp_index = 999
        for i in range(len(self.occurrence)):
            if self.occurrence[i] == 1 and self.exist[i] < temp_index:
                temp_index = self.exist[i]
        if temp_index == 999:
            return -1
        else:
            return temp_index

    def char_to_index(self, c):
        return ord(c) - 97

print(Solution().firstUniqChar("cc"))

