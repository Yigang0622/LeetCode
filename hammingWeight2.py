# LeetCode
# hammingWeight2 
# Created by Yigang Zhou on 2020/9/6.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 二进制中1的个数
# https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            if n % 2 == 1:
                count += 1
            n = n // 2

        return count

s = Solution().hammingWeight(0b1101)
print(s)