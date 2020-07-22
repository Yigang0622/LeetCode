# 排列硬币

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 0:
            return 0
        i = 1
        while n > i:
            n -= i
            i += 1
        print(i)
        return i

Solution().arrangeCoins(3)