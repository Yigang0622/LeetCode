# LeetCode
# coinChange 
# Created by Yigang Zhou on 2020/8/1.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


# 零钱兑换
# https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvf0kh/

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


coins = [5,3,6,1]
amount = 10
r = Solution().coinChange(coins, amount)
print(r)
