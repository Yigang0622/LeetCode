# LeetCode
# getSmallestString 
# Created by Yigang Zhou on 2021/1/30.
# Copyright © 2021 Yigang Zhou. All rights reserved.

# 1663. 具有给定数值的最小字符串
# https://leetcode-cn.com/problems/smallest-string-with-a-given-numeric-value/
import collections


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z']

        q = collections.deque()
        n_left = n
        while k >= 26:
            right_most = 26
            while k - right_most < n_left - 1:
                right_most -= 1
            # print(alphabet[right_most-1])
            q.appendleft(alphabet[right_most - 1])
            k -= right_most
            n_left -= 1

        # print(n_left, k)
        if k > n_left:
            # print(alphabet[k - n_left])

            q.appendleft(alphabet[k - n_left])
            n_left -= 1

        while n_left > 0:
            q.appendleft('a')
            n_left -= 1
            # print(['a'] * (n_left - 1))
        # else:
        #     print(['a'] * (n_left))
        return ''.join(q)


n = 97961
k = 2516030
r = Solution().getSmallestString(n, k)
print(r)
