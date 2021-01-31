# LeetCode
# brokenCalc 
# Created by Yigang Zhou on 2021/1/31.
# Copyright © 2021 Yigang Zhou. All rights reserved.

# 991. 坏了的计算器
# https://leetcode-cn.com/problems/broken-calculator/

# 双倍（Double）：将显示屏上的数字乘 2；
# 递减（Decrement）：将显示屏上的数字减 1 。

class Solution:

    def brokenCalc(self, X: int, Y: int) -> int:
        # 除2 递增倒推
        count = 0
        while Y > X:
            while Y % 2 == 0 and Y / 2 > X:
                Y = Y / 2
                count += 1
                print(Y)
            if Y % 2 != 0:
                Y = Y - 1
                count += 1
                print(Y)


X = 3
Y = 10

r = Solution().brokenCalc(X, Y)
print(r)
