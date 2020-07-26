# LeetCode
# permution
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        self.dfs([], nums, len(nums), answer)
        return answer

    def dfs(self, current: List[int], possible_choice: List[int], target_len: int, answer):
        if len(current) == target_len:
            answer.append(current)
        else:
            for each in possible_choice:
                if each not in current:
                    a = current[:]
                    a.append(each)
                    self.dfs(a, possible_choice, target_len, answer)


s = Solution().permute([1,2,3,4])


