# LeetCode
# movingCount 
# Created by Yigang Zhou on 2020/9/5.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 机器人的运动范围
# https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
import collections
import common.arrayCommon as Array


class Solution:

    def vaildNextStep(self, visited, m, n, i, j, k):
        # 越界
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        # 走过了
        if (i,j) in visited:
            return False

        coord_digit_sum = 0
        while i > 0:
            coord_digit_sum += i % 10
            i = i // 10

        while j > 0:
            coord_digit_sum += j % 10
            j = j // 10
        return coord_digit_sum <= k

    def movingCount(self, m: int, n: int, k: int) -> int:
        q = collections.deque()
        q.append((0, 0))
        visited = set()
        visited.add((0,0))
        while (q):
            i, j = q.popleft()
            visited.add((i,j))

            for i_next, j_next in [(i + 1, j), (i, j + 1)]:
                if self.vaildNextStep(visited, m, n, i_next, j_next, k):
                    visited.add((i_next, j_next))
                    q.append((i_next, j_next))
        return len(visited)


m = 36
n = 11
k = 15
r = Solution().movingCount(m, n, k)
print(r)
