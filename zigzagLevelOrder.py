# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/32/trees-and-graphs/86/
from typing import List

from common.treeCommon import *
import collections

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        ans = []
        self.search(root, 0, ans)
        ans = [list(x) for x in ans]
        return ans

    def search(self, node, depth, ans):
        if not node:
            return

        if len(ans) < depth + 1:
            q = collections.deque()
            q.append(node.val)
            ans.append(q)
        else:
            if depth % 2 == 0:
                ans[depth].append(node.val)
            else:
                ans[depth].appendleft(node.val)

        self.search(node.left, depth+1,ans)
        self.search(node.right, depth+1,ans)


n = test_tree()
r = Solution().zigzagLevelOrder(n)
print(r)