# LeetCode
# isNStraightHand 
# Created by Yigang Zhou on 2020/9/6.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 一手顺子
# https://leetcode-cn.com/problems/hand-of-straights/
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand.sort()
        temp = []
        while len(hand):
            if len(temp) == 0:
                temp.append(hand[0])
                hand.remove(hand[0])

            for _ in range(W-1):
                target = temp[-1] + 1
                if target in hand:
                    temp.append(target)
                    hand.remove(target)
                else:
                    return False
            temp = []
        return True



hand = [1,2,3,4,5]
W = 4
s = Solution().isNStraightHand(hand, W)
print(s)