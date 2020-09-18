# LeetCode
# validateStackSequences 
# Created by Yigang Zhou on 2020/9/15.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 剑指 Offer 31. 栈的压入、弹出序列
# https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        i = 0
        for each in pushed:
            s.append(each)
            print('push', each)
            while s and s[-1] == popped[i]:
                e = s.pop()
                print('pop',e)
                i+=1
        return not s


pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
r = Solution().validateStackSequences(pushed, popped)