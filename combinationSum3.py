# LeetCode
# combinationSum3 
# Created by Yigang Zhou on 2020/8/25.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 组合总和 III
# https://leetcode-cn.com/problems/combination-sum-iii/
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.search(k,n,set(),1,ans)
        return ans

    def search(self,k,n,current,last,ans):

        if len(current) < k and sum(current) >= n:
            return

        if len(current) == k:
            if sum(current) == n:
                ans.append(list(current))
            return
        for i in range(last, 10):
            if i not in current:
                current.add(i)
                self.search(k,n,current,i,ans)
                current.remove(i)



k = 3
n = 15
r = Solution().combinationSum3(k, n)
print(r)