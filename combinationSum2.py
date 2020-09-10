from typing import List

# 组合总和 II
# https://leetcode-cn.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.search([], candidates, 0, target, ans)
        return ans


    def search(self, current, candidates, start, target, ans):
        s = sum(current)
        if s >= target:
            if s == target:
                ans.append(current[:])
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            current.append(candidates[i])
            self.search(current, candidates, i+1, target, ans)
            current.pop()




candidates = [10,1,2,7,6,1,5]
target = 8
r = Solution().combinationSum2(candidates, target)
print(r)