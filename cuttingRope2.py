# LeetCode
# cuttingRope2 
# Created by Yigang Zhou on 2020/9/6.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 剪绳子II
# https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        elif n == 3:
            return 2

        numOfThree = n // 3

        if n - numOfThree * 3 == 1: #留4
            numOfThree -= 1

        numOfTwo = (n - numOfThree * 3)//2

        return 3 ** numOfThree * 2 ** numOfTwo


s = Solution().cuttingRope(8)
print(s)