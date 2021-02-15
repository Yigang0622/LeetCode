# LeetCode
# maximumSwap 
# Created by Yigang Zhou on 2021/1/30.
# Copyright © 2021 Yigang Zhou. All rights reserved.

# 670. 最大交换
# https://leetcode-cn.com/problems/maximum-swap/


class Solution:
    def maximumSwap(self, num: int) -> int:
        s = [x for x in str(num)]
        for i in range(len(s)):
            max = s[-1]
            max_idx = len(s) - 1
            for j in range(len(s) - 1, i, -1):
                if s[j] > max:
                    max_idx = j
                    max = s[j]
            if s[max_idx] > s[i]:
                s[max_idx], s[i] = s[i], s[max_idx]
                return int(''.join(s))

        return int(''.join(s))


num = 123456789
r = Solution().maximumSwap(num)
print(r)