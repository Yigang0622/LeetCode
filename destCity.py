# LeetCode
# destCity 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# https://leetcode-cn.com/problems/destination-city/
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        for path in paths:
            for each in path:
                if each in s:
                    s.remove(each)
                else:
                    s.add(each)
        print(s)

Solution().destCity([["B","C"],["D","B"],["C","A"]])