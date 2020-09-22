from typing import List

# 1043. 分隔数组以得到最大和
# https://leetcode-cn.com/problems/partition-array-for-maximum-sum/

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n
        dp[0] = arr[0]
        for i in range(1, n):
            m = arr[i]
            for j in range(k):
                if i - j >= 0:
                    m = max(m, arr[i - j])
                    if i - j - 1 < 0:
                        dp[i] = max(dp[i], (j + 1) * m)
                    else:
                        dp[i] = max(dp[i], dp[i - j - 1] + (j + 1) * m)

        return dp[-1]


A = [1,15,7,9,2,5,10]
K = 3
r = Solution().maxSumAfterPartitioning(A, K)