# 991. 坏了的计算器
# https://leetcode-cn.com/problems/broken-calculator/

# 在显示着数字的坏计算器上，我们可以执行以下两种操作：
#
# 双倍（Double）：将显示屏上的数字乘 2；
# 递减（Decrement）：将显示屏上的数字减 1 。
# 最初，计算器显示数字 X。
#
# 返回显示数字 Y 所需的最小操作数。

# 转换为 / 2 与 +1 问题

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if Y < X:
            return X - Y
        else:
            op_count = 0
            while X != Y:
                if Y % 2 == 0 and Y > X:
                    op_count += 1
                    Y = Y / 2
                    print('/2', Y)
                else:
                    op_count += 1
                    Y = Y + 1
                    print('+1', Y)
            return op_count


X = 3
Y = 10
r = Solution().brokenCalc(X, Y)
print(r)
