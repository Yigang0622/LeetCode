# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from common.treeCommon import TreeNode

# 106. 从中序与后序遍历序列构造二叉树
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        print(inorder, postorder)

        if len(inorder) <= 0 or len(postorder) <= 0:
            return None
        val = postorder[-1]
        node = TreeNode(postorder[-1])
        i = inorder.index(val)
        print(i)
        inorder_left = inorder[:i]
        inorder_right = inorder[i+1:]
        postorder_left = postorder[:i]
        postorder_right = postorder[i:-1]
        node.left = self.buildTree(inorder_left, postorder_left)
        node.right = self.buildTree(inorder_right, postorder_right)
        return node


inorder = [1, 2]
postorder = [2, 1]
r = Solution().buildTree(inorder, postorder)
a = 1
