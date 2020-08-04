# https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xwxa3m/
# 二叉树的序列化与反序列化

from common.treeCommon import *


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        d = self.depth(root)
        arr = ['x' for i in range(2 ** d - 1)]
        self._serialize(root, arr, 0)
        serialized = ''
        for i, each in enumerate(arr):
            serialized += str(each)
            if i is not len(arr) - 1:
                serialized += ','
        return serialized

    def _serialize(self, node, arr, i):
        if not node:
            return
        arr[i] = node.val
        self._serialize(node.left, arr, i * 2 + 1)
        self._serialize(node.right, arr, i * 2 + 2)

    def depth(self, node, depth=0):
        if not node:
            return depth
        return max(self.depth(node.left, depth + 1), self.depth(node.right, depth + 1))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        arr = []
        for each in data.split(','):
            if each is 'x':
                arr.append(None)
            else:
                arr.append(int(each))

        print('!', arr)
        root = self._deserialize(TreeNode(-1), 0, arr)
        return root

    def _deserialize(self, node, i, arr):
        if i < 0 or i >= len(arr):
            return None
        if arr[i] is None:
            return None
        node.val = arr[i]
        node.left = self._deserialize(TreeNode(-1), i * 2 + 1, arr)
        node.right = self._deserialize(TreeNode(-1), i * 2 + 2, arr)
        return node


tree = [-1,0,1]
root = genTree(tree)
c = Codec()
s = c.serialize(root)
print(s)
r = c.deserialize(s)
a = 1