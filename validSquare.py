# LeetCode
# validSquare 
# Created by Yigang Zhou on 2020/10/7.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


# 593. 有效的正方形
# https://leetcode-cn.com/problems/valid-square/

class Solution:

    def distance(self, p1, p2):
        return ((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2) ** 0.5

    # p1,2对角线 p3,4对角线
    def validSquareHelper(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # 对角线相等且四条边相等
        return self.distance(p1, p3) == self.distance(p1, p4) == self.distance(p2, p3) == self.distance(p2, p4) \
               and self.distance(p1, p2) == self.distance(p3, p4)

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # 边长不为0
        if self.distance(p1, p2) == 0:
            return False
        return self.validSquareHelper(p1, p2, p3, p4) or \
               self.validSquareHelper(p1, p3, p2, p4) or \
               self.validSquareHelper(p1, p4, p3, p2) or \
               self.validSquareHelper(p2, p4, p3, p1)


p1 = [0, 0]
p2 = [1, 1]
p3 = [1, 0]
p4 = [0, 1]

r = Solution().validSquare(p1, p2, p3, p4)
print(r)
