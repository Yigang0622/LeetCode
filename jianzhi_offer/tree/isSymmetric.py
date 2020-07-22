from jianzhi_offer.tree.common import *


class Solution:

    depth = 0


    def isSymmetric(self, root: TreeNode) -> bool:
        self.depth = 0
        self.iterTree(root, 0)
        print('final', self.depth)

    def iterTree(self, node: TreeNode, depth):
        self.depth = depth
        if node:
            self.depth += 1
            self.iterTree(node.left, depth + 1)
            print(node.val)
            self.iterTree(node.right, depth + 1)


arr = [1, 2, 2, None, 3, None, 3]
root = genTree(arr)
s = Solution().isSymmetric(root)
print('ans', s)
