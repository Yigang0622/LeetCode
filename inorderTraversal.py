# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/32/trees-and-graphs/85/
from typing import List

from common.treeCommon import *


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.inorder(root, ans)
        return ans

    def inorder(self, node: TreeNode, ans: List[int]):
        if not node:
            return
        self.inorder(node.left, ans)
        ans.append(node.val)
        self.inorder(node.right, ans)



tree_arr = [1,2,3,4,5,6,7]
root = genTree(tree_arr)
r = Solution().inorderTraversal(root)
print(r)