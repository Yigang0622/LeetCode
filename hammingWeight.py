# 位1的个数
# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn1m0i/

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n is not 0:
            count += n & 1
            n = n >> 1
        return count



r = Solution().hammingWeight(0b1111)
print(r)