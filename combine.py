# LeetCode
# combine 
# Created by Yigang Zhou on 2020/9/8.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 组合
# https://leetcode-cn.com/problems/combinations/
from typing import List
import collections


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        q = collections.deque()
        for i in range(1, n + 1):
            q.append([i])

        while q:
            e = q.popleft()
            if len(e) == k:
                q.appendleft(e)
                break
            else:
                for i in range(e[-1] + 1, n + 1):
                    a = e[:]
                    a.append(i)
                    q.append(a)
        return list(q)


n = 3
k = 3
r = Solution().combine(n, k)
print(r)
