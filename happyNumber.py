# 快乐数
# https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xw99u7/

class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()
        while n not in history and n > 0:
            history.add(n)
            n = self.nextNumber(n)
        return n == 1


    def nextNumber(self, n) -> int:
        sum = 0
        while n > 0:
            n, reminder = divmod(n, 10)
            sum += reminder ** 2
        return sum


r = Solution().isHappy(18)
print(r)