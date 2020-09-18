# LeetCode
# permuteUnique 
# Created by Yigang Zhou on 2020/9/18.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 47. 全排列 II
# https://leetcode-cn.com/problems/permutations-ii/
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = [0] * len(nums)
        nums.sort()
        self.dfs([], visited,0,nums,ans)
        return ans

    def dfs(self, current, visited, i, nums, ans):
        if i == len(nums):
            ans.append(current[:])
            return
        for j, each in enumerate(nums):
            if visited[j] == 1 or (j > 0 and nums[j] == nums[j - 1] and visited[j - 1] == 0):
                continue
            visited[j] = 1
            current.append(each)
            self.dfs(current, visited, i+1, nums, ans)
            visited[j] = 0
            current.pop()

nums = [1,1,2]
r = Solution().permuteUnique(nums)
print(r)