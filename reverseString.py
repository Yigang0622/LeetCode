# LeetCode
# reverseString 
# Created by Yigang Zhou on 2020/10/8.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 344. 反转字符串
# https://leetcode-cn.com/problems/reverse-string/
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        for i in range(N//2):
            s[i],s[N-i-1] = s[N-i-1],s[i]


s = ["H","a","n","n","a","h"]
Solution().reverseString(s)
print(s)
