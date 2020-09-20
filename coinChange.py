from typing import List


# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/51/dynamic-programming/106/

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            min_num = amount + 1
            for coin in coins:
                if i - coin >= 0:
                    min_num = min(min_num, dp[i-coin] + 1)
            dp[i] = min_num
        if dp[-1] == amount + 1:
            return -1
        return dp[-1]

coins = [2]
amount = 3

r = Solution().coinChange(coins, amount)
