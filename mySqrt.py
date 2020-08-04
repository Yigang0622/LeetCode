# https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xwrzwc/
# 实现平方根

class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 0:
            return 0

        err = 0.5
        root_square = x
        while abs(x - root_square * root_square) > err:
            root_square = (x / root_square + root_square) / 2
        return int(root_square)


r = Solution().mySqrt(3)
print(r)