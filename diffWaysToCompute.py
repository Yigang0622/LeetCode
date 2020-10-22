# LeetCode
# diffWaysToCompute 
# Created by Yigang Zhou on 2020/10/19.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List

# 241. 为运算表达式设计优先级
# https://leetcode-cn.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]

        oprands = ['+','-','*']
        res = []
        for i, each in enumerate(input):
            if each in oprands:
                left_combinations = self.diffWaysToCompute(input[:i])
                right_combinations = self.diffWaysToCompute(input[i+1:])
                for l in left_combinations:
                    for r in right_combinations:
                        res.append(eval('{}{}{}'.format(l, each, r)))
        return res



input = "2*3-4*5"
s = Solution().diffWaysToCompute(input)
print(s)