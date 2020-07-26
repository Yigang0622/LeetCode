from common.treeCommon import *


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isTwoNodeSymmetric(root, root)

    def isTwoNodeSymmetric(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val == right.val and self.isTwoNodeSymmetric(left.left, right.right) and self.isTwoNodeSymmetric(left.right, right.left)



arr = [1,2,2,3,4,4,3]
root = genTree(arr)
s = Solution().isSymmetric(root)
print('ans', s)
