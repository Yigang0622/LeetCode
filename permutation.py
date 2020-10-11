# LeetCode
# permutation 
# Created by Yigang Zhou on 2020/10/9.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 剑指 Offer 38. 字符串的排列
# https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        visited = [0] * len(s)
        ans = set()
        self.search("", visited, 0, s, ans)
        return list(ans)

    def search(self, current,visited, step, s, ans):
        if step == len(s):
            ans.add(current)
            return
        se = set()
        for i in range(len(s)):
            if visited[i] == 0:
                if s[i] not in se:
                    visited[i] = 1
                    s_new = current + s[i]
                    se.add(s[i])
                    self.search(s_new, visited, step + 1, s, ans)
                    visited[i] = 0


r= Solution().permutation("abc")
print(r)