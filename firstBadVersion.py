# LeetCode
# firstBadVersion 
# Created by Yigang Zhou on 2020/8/1.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnto1s/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(self):
    return False

class Solution:

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left



s = Solution().firstBadVersion(9)