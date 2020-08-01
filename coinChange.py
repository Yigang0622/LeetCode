from typing import List
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/51/dynamic-programming/106/

class Solution:

    should_stop = False

    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        self.should_stop = False
        coins = sorted(coins, reverse=True)
        ans = []
        self.search([], coins, amount, ans)
        print(ans)
        if len(ans) == 0:
            return -1
        else:
            return len(ans)

    def search(self, current, available_coins, target, ans):
        if self.should_stop:
            return

        if target <= 0:
            if target == 0:
                self.should_stop = True
                ans.extend(current)
            return

        for each in available_coins:
            current.append(each)
            self.search(current, available_coins, target - each, ans)
            current.pop()

coins = [5,1]
amount = 99

r = Solution().coinChange(coins, amount)
