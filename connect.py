# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/32/trees-and-graphs/88/

from common.treeCommon import *


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        ans = []
        self.search(root, 0, ans)
        return root

    def search(self, node, depth, ans):
        if not node:
            return

        if len(ans) < depth + 1:
            ans.append([node])
        else:
            ans[depth][len(ans[depth]) - 1].next = node
            ans[depth].append(node)

        self.search(node.left, depth+1,ans)
        self.search(node.right, depth+1,ans)


n = test_tree()
r = Solution().connect(n)
print(r)