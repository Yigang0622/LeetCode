from common.treeCommon import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root = self.buildNode(TreeNode(0), preorder, inorder)
        return root

    def buildNode(self, node: TreeNode, preorder: List[int], inorder: List[int]):
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        node.val = preorder[0]
        i = inorder.index(node.val)
        left_inorder = inorder[:i]
        right_inorder = inorder[i + 1:]
        left_inorder_len = len(left_inorder)
        left_preorder = preorder[1:left_inorder_len + 1]
        right_preorder = preorder[left_inorder_len + 1:]
        node.left = self.buildNode(TreeNode(0), left_preorder, left_inorder)
        node.right = self.buildNode(TreeNode(0), right_preorder, right_inorder)
        return node


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
r = Solution().buildTree(preorder, inorder)
