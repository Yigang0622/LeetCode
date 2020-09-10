# LeetCode
# dailyTemperatures 
# Created by Yigang Zhou on 2020/9/9.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 每日温度
# https://leetcode-cn.com/problems/daily-temperatures/
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        s = []
        ans = [0] * len(T)
        for i,each in enumerate(T):
            if not s:
                s.append(i)
            else:
                while s and each > T[s[-1]]:
                    j = s.pop()
                    ans[j] = i - j
                s.append(i)
        return ans



temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
s = Solution().dailyTemperatures(temperatures)
print(s)