# LeetCode
# lengthOfLongestSubstring 
# Created by Yigang Zhou on 2020/9/29.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 3. 无重复字符的最长子串
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(s)
        d = dict()
        left = 0
        len = 0
        for i, c in enumerate(s):
            right = i
            if c not in d:
                d[c] = i
            else:
                # 防止 abba的最后一个a使得做指针前移，所以先做比较
                if d[c] + 1 > left:
                    left = d[c] + 1
                d[c] = i
            print(left, right)
            len = max(len, right - left + 1)
        print(len)
        return len


s = "abba"
r = Solution().lengthOfLongestSubstring(s)
