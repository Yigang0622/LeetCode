from common.treeCommon import *


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr = []
        self.dfs(root, arr)
        return arr[k-1]

    def dfs(self, node: TreeNode, result):
        if node is None:
            return
        self.dfs(node.left, result)
        result.append(node.val)
        self.dfs(node.right, result)

root = genTree([5,3,6,2,4,None,None,1])
Solution().kthSmallest(root,3)