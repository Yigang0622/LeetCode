from common.treeCommon import *

# 验证二叉搜索树

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def verify(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not verify(node.right, val, upper):
                return False
            if not verify(node.left, lower, val):
                return False
            return True

        return verify(root)



arr = [3,9,20, None, None,15,7]
root = genTree(arr)
s = Solution().isValidBST(root)
print('ans',s)