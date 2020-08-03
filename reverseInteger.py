# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnx13t/

class Solution:
    def reverse(self, x: int) -> int:

        neg = x < 0
        mutiplyer = []
        digits = []
        m = 1
        x = abs(x)

        while m <= x:
            digit = x // m % 10
            mutiplyer.append(m)
            digits.append(digit)
            m *= 10
        sum = 0
        for i, m in enumerate(reversed(mutiplyer)):
            sum += digits[i] * m
        if neg:
            sum = -sum

        if sum > 2147483647 or sum < -2147483648:
            return 0
        else:
            return sum


r = Solution().reverse(10)
print(r)