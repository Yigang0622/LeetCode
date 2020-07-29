from typing import List
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/49/backtracking/94/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)+1):
            self.search(0, [], nums, i, ans)
        return ans

    def search(self, start, current, nums, target_len, ans):
        if len(current) == target_len:
            ans.append(current[:])
            return
        for i in range(start, len(nums)):
            current.append(nums[i])
            self.search(i+1, current, nums, target_len, ans)
            current.pop()



a = [1,2,3,4]
r = Solution().subsets(a)