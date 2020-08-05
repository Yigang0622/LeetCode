# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdhfe5/
# 二叉树中的最大路径和
from common.treeCommon import *


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return 0