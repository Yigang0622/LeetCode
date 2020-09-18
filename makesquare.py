# 火柴拼正方形
# https://leetcode-cn.com/problems/matchsticks-to-square/
from typing import List


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not len(nums):
            return False
        if sum(nums) % 4 != 0:
            return False
        # 目标边长
        target_edge = sum(nums) // 4
        for each in nums:
            if each > target_edge:
                return False

        self.solved = False
        # 倒排序，使得dfs提前剪枝
        nums = sorted(nums, reverse=True)
        self.search([[], [], [], []], nums, 0, target_edge)
        return self.solved

    def search(self, four_edges, nums, i, target_edge_len):
        if self.solved:
            return
        if sum(four_edges[0]) > target_edge_len or  sum(four_edges[1]) > target_edge_len or  sum(four_edges[2]) > target_edge_len or  sum(four_edges[3]) > target_edge_len:
            # 如果搜索中发现任意一边长于正方形长度，剪枝
            return False
        if len(four_edges[1]) > 0 and len(four_edges[0]) == 0:
            return
        if len(four_edges[2]) > 0 and len(four_edges[1]) == 0:
            return
        if len(four_edges[3]) > 0 and len(four_edges[2]) == 0:
            return

        if len(nums) == i:
            if sum(four_edges[0]) == sum(four_edges[1]) == sum(four_edges[2]) == sum(four_edges[3]):
                self.solved = True
            return

        for x in [0, 1, 2, 3]:
            four_edges[x].append(nums[i])
            self.search(four_edges, nums, i + 1, target_edge_len)
            four_edges[x].pop()


nums = [12,12,12,16,20,24,28,32,36,40,44,48,52,56,60]
r = Solution().makesquare(nums)
print(r)
