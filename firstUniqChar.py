# LeetCode
# firstUniqChar 
# Created by Yigang Zhou on 2020/9/5.
# Copyright © 2020 Yigang Zhou. All rights reserved.

#  第一个只出现一次的字符
# https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
class Solution:
    def firstUniqChar(self, s: str) -> str:
        arr = [ord(x) for x in s]
        print(arr)



s = Solution()
s.firstUniqChar('abaccdeff')
