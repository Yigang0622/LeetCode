from typing import List

# 组合总和 II
# https://leetcode-cn.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.search([], candidates, target)


    def search(self, current, candidates, target):
        s = sum(current)
        if s >= target:

            if s == target:
                print(current)
                pass
            return

        c = candidates[:]
        for each in c:
            current.append(each)
            c.remove(each)
            self.search(current, c, target)
            current.pop()




candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
r = Solution().combinationSum2(candidates, target)