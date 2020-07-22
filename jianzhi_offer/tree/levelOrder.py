from jianzhi_offer.tree.common import *

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.iterTree(root, 0, result)
        return result

    def iterTree(self, node, depth, result):
        if node is None:
            return
        if len(result) - 1 < depth:
            result.append([node.val])
        else:
            result[depth].append(node.val)
        self.iterTree(node.left, depth+1, result)
        self.iterTree(node.right, depth+1, result)


arr = [3,9,20,None,None,15,7]
root = genTree(arr)
s = Solution().levelOrder(root)