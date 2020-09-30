# LeetCode
# isFlipedString 
# Created by Yigang Zhou on 2020/9/28.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 面试题 01.09. 字符串轮转
# https://leetcode-cn.com/problems/string-rotation-lcci/

class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        # 如果是轮转的话,s1会出现在两个s2拼在一起的字符串中
        # erbottlewat + erbottlewat -> er bottlewater bottlewat
        return s1 in s2 + s2


s1 = "waterbottle"
s2 = "erbottlewat"