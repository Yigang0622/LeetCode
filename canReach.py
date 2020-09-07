# LeetCode
# canReach 
# Created by Yigang Zhou on 2020/9/6.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 跳跃游戏3
# https://leetcode-cn.com/problems/jump-game-iii/
from typing import List
import collections

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        N = len(arr)
        visited = set()
        q = collections.deque()
        visited.add(start)
        q.append(start)

        while(q):
            e = q.popleft()
            if arr[e] == 0:
                return True
            visited.add(e)
            l = e - arr[e]
            if l >= 0 and l not in visited:
                q.append(l)

            r = e + arr[e]
            if r< N and r not in visited:
                q.append(r)

        return False



arr = [4,2,3,0,3,1,2]
start = 0

s = Solution().canReach(arr, start)
print(s)