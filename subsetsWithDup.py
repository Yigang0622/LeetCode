# LeetCode
# subsetsWithDup 
# Created by Yigang Zhou on 2020/9/23.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 90. 子集 II
# https://leetcode-cn.com/problems/subsets-ii/
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.dfs([],0,nums,ans)
        print(ans)
        return ans

    def dfs(self, current, i, nums, ans):
        print(current)
        ans.append(current[:])

        for j in range(i, len(nums)):
            if j > i and nums[j-1] == nums[j]:
                continue
            current.append(nums[j])
            self.dfs(current, j+1, nums, ans)
            current.pop()


nums = [1,2,2]
r = Solution().subsetsWithDup(nums)



