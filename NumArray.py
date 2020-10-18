# LeetCode
# NumArray 
# Created by Yigang Zhou on 2020/10/18.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 307. 区域和检索 - 数组可修改
# https://leetcode-cn.com/problems/range-sum-query-mutable/
from typing import List


# 线段树
class NumArray:

    def __init__(self, nums: List[int]):
        if not len(nums):
            return
        self.nums = nums
        self.tree = [-1] * 20
        self.buildTree(self.nums, 0, len(nums) - 1, self.tree, 0)
        # print(self.tree)

    def buildTree(self, arr, l, r, tree, i):
        if l == r:
            tree[i] = arr[l]
            return arr[l]
        else:
            mid = (l + r) // 2
            tree_l = 2 * i + 1
            tree_r = 2 * i + 2
            left_sum = self.buildTree(arr, l, mid, tree, tree_l)
            right_sum = self.buildTree(arr, mid + 1, r, tree, tree_r)
            tree[i] = left_sum + right_sum
            return tree[i]

    def update(self, i: int, val: int) -> None:
        self.update_tree(i, val, 0, len(self.nums) - 1, 0)
        # print(self.tree)

    def update_tree(self, i, val, l, r, tree_i):
        if i < l or i > r:
            return self.tree[tree_i]
        else:
            if l == r:
                self.nums[i] = val
                self.tree[tree_i] = val
                return val
            else:
                mid = (l + r) // 2
                tree_l = 2 * tree_i + 1
                tree_r = 2 * tree_i + 2
                left_sum = self.update_tree(i, val, l, mid, tree_l)
                right_sum = self.update_tree(i, val, mid + 1, r, tree_r)
                self.tree[tree_i] = left_sum + right_sum
                return self.tree[tree_i]

    def sumRange(self, i: int, j: int) -> int:
        result = self.sum_range(i, j, 0, len(self.nums) - 1, 0)
        # print('result', result)
        return result

    def sum_range(self, i, j, l, r, tree_i):
        # print(l,r,'entry')
        if j < l or i > r:
            return 0
        elif l >= i and r <= j:
            # print(l, r, self.tree[tree_i])
            return self.tree[tree_i]
        else:
            if l == r:
                return self.tree[tree_i]
            else:
                mid = (l + r) // 2
                tree_l = 2 * tree_i + 1
                tree_r = 2 * tree_i + 2
                left_sum = self.sum_range(i, j, l, mid, tree_l)
                right_sum = self.sum_range(i, j, mid + 1, r, tree_r)
                return left_sum + right_sum


# Your NumArray object will be instantiated and called as such:
nums = [1, 2, 3, 4, 5, 6]
obj = NumArray(nums)
obj.update(0, 2)
r = obj.sumRange(0, 2)
print(r)
# param_2 = obj.sumRange(i,j)
