# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common.treeCommon import *


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        root = self.buildNode(nums, TreeNode(0))
        return root


    def buildNode(self, nums:List[int], node:TreeNode):
        if len(nums) == 0:
            return None
        mid = int(len(nums) / 2)
        node.val = nums[mid]
        node.left = self.buildNode(nums[:mid], TreeNode(0))
        node.right = self.buildNode(nums[mid+1:], TreeNode(0))
        return node



arr = [-10,-3,0,5,9]
r = Solution().sortedArrayToBST(arr)