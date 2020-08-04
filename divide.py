# 两数相处
# https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xwp6vi/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0 or dividend == 0:
            return 0
        if divisor == dividend:
            return 1

        if abs(dividend) < abs(divisor):
            return 0

        if abs(divisor) == 1:
            return dividend * divisor

        result = 0
        sum = 0
        while sum < abs(dividend):
            sum += abs(divisor)
            if sum <= abs(dividend):
                result += 1

        if divisor < 0 and dividend > 0:
            return -result
        elif divisor > 0 and dividend < 0:
            return -result
        else:
            return result


r = Solution().divide(-7, -1)
print(r)