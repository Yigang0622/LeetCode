# LeetCode
# isUgly 
# Created by Yigang Zhou on 2020/10/19.
# Copyright © 2020 Yigang Zhou. All rights reserved.

class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False

        while num % 5 == 0:
            num = num / 5
        while num % 3 == 0:
            num = num / 3
        while num % 2 == 0:
            num = num / 2
        return num == 1

s = Solution().isUgly(14)
print(s)
