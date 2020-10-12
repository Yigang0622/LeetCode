# https://leetcode-cn.com/problems/chou-shu-lcof/
# 剑指 Offer 49. 丑数

class Solution:
    def nthUglyNumber(self, n: int) -> int:

        base = [2, 3, 5]
        for each in base:
            n = each
            # while


r = Solution().nthUglyNumber(10)
