# 汉明距离
# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnyode/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        while x is not 0 and y is not 0:
            if not x & 1 == y&1:
                distance += 1
            x = x >> 1
            y = y >> 1
        return distance


r = Solution().hammingDistance(999, 11)
print(r)
