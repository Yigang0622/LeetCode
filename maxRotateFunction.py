# 396. 旋转函数
# https://leetcode-cn.com/problems/rotate-function/
from typing import List


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        n = len(A)
        if n == 0:
            return 0
        ans = -float('inf')
        for offset in range(n):
            ans_temp = 0
            for i, each in enumerate(A):
                factor = i + offset
                if factor >= n:
                    factor -= n
                ans_temp += factor*each
            ans = max(ans, ans_temp)
        # print(ans)
        return ans

A = [4, 3, 2, 6]
r = Solution().maxRotateFunction(A)
print(r)