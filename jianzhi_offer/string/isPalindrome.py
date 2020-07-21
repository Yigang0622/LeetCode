# LeetCode
# isPalindrome 
# Created by Yigang Zhou on 2020/7/21.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        s_new = ''
        for each in s.lower():
            if 97 <= ord(each) <= 122 or 48 <= ord(each) <= 57:
                s_new += each
        iter_count = int(len(s_new)/2)
        length = len(s_new)

        for i in range(iter_count):
            if s_new[i] != s_new[length - i - 1]:
                return False
        return True


r = Solution().isPalindrome('"0P"')
print(r)