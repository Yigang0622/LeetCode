# LeetCode
# fourSumCount 
# Created by Yigang Zhou on 2020/7/27.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# https://leetcode-cn.com/explore/interview/card/top-interview-questions/268/hash-map/1163/
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        counter = {}
        count = 0

        for a in A:
            for b in B:
                s = a + b
                if s in counter:
                    counter[s] += 1
                else:
                    counter[s] = 1

        for c in C:
            for d in D:
                sum = - (c + d)
                if sum in counter:
                    counter += counter[sum]

        return count