# 组合总和
# https://leetcode-cn.com/problems/combination-sum/
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        self.search([], 0, 0, n, ans, sorted(candidates), target)
        return ans

    def search(self, current, current_sum, begin, n, ans, candidates, target):
        if current_sum >= target:
            if current_sum == target:
                ans.append(current[:])
            return

        for i in range(begin, n):
            if current_sum + candidates[i] > target:
                break
            current.append(candidates[i])
            self.search(current, current_sum + candidates[i], i, n, ans, candidates, target)
            current.pop()


candidates = [8,7,4,3]
target = 11
r = Solution().combinationSum(candidates, target)
print(r)