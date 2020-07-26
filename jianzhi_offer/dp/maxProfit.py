from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        buy_in_price = -prices[0]
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            if -prices[i] > buy_in_price:
                buy_in_price = -prices[i]
            else:
                dp[i] = buy_in_price + prices[i]
        print(max(dp))
        return max(dp)

arr = [1,6,4,3,1]
Solution().maxProfit(arr)
