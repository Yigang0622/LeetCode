# LeetCode
# pyramidTransition 
# Created by Yigang Zhou on 2020/9/13.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 金字塔转换矩阵
# https://leetcode-cn.com/problems/pyramid-transition-matrix/
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        next = {}
        for each in allowed:
            k = each[:2]
            v = each[-1]
            if k in next:
                next[k].append(v)
            else:
                next[k] = [v]
        self.get_next_level(bottom, next)

    def get_next_level(self, bottom, next):
        next_bottom = []
        for i in range(1,len(bottom)):
            k = bottom[i-1]+bottom[i]
            if k in next:
                next_bottom.append(next[k])
            else:
                next_bottom.append([])
        print(next_bottom)
        ans = []
        self.dfs_bottoms([],0,next_bottom,ans)
        print(ans)
        return ans

    def dfs_bottoms(self, curr,i, next_bottom_arr, ans):
        if len(next_bottom_arr) == i:
            ans.append(curr[:])
            return
        for each in next_bottom_arr[i]:
            curr.append(each)
            self.dfs_bottoms(curr,i+1,next_bottom_arr, ans)
            curr.pop()


bottom = "AABA"
allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
r = Solution().pyramidTransition(bottom, allowed)