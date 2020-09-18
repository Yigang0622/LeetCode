# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from common.treeCommon import TreeNode
import common.treeCommon as Tree


class NodeWithCoord:

    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y

    def __lt__(self, other):
        if other.x != self.x:
            return self.x < other.x
        elif other.y != self.y:
            return self.y < other.y
        else:
            return self.val < other.val

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = []
        self.inorder(root, 0, 0, nodes)
        nodes.sort()

        last_x = nodes[0].x
        ans = [[]]
        for each in nodes:
            if each.x != last_x:
                ans.append([])
            ans[-1].append(each.val)
            last_x = each.x
        print(ans)
        return ans

    def inorder(self, node, x, y, nodes):
        if not node:
            return
        self.inorder(node.left, x - 1, y + 1, nodes)
        n = NodeWithCoord(node.val, x, y)
        nodes.append(n)
        self.inorder(node.right, x + 1, y + 1, nodes)


root = Tree.genTree([1,2,3,4,5,6,7])
r = Solution().verticalTraversal(root)