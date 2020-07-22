from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = -prices[0]
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            print(prices[i])
            dp[i] = max(cost+prices[i], -prices[i])


arr = [7,1,5,3,6,4]
Solution().maxProfit(arr)