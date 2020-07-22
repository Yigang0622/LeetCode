from jianzhi_offer.tree.common import *

class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
            return max(leftDepth, rightDepth) + 1





arr = [1,2,3,4,5]
root = genTree(arr)
s = Solution().maxDepth(root)
print(s)