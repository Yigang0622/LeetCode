# LeetCode
# isAnagram 
# Created by Yigang Zhou on 2020/7/21.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
# 说明:
# 你可以假设字符串只包含小写字母。
#
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        occurrence = [0] * 26
        print(s,t)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            occurrence[self.char_to_index(s[i])] += 1

        for i in range(len(t)):
            occurrence[self.char_to_index(t[i])] -= 1
        for each in occurrence:
            if each != 0:
                return False
        return True

    def char_to_index(self, c):
        return ord(c) - 97

print(Solution().isAnagram('anagram','anagrag'))