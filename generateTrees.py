# LeetCode
# generateTrees 
# Created by Yigang Zhou on 2020/11/7.
# Copyright © 2020 Yigang Zhou. All rights reserved.


# 95. 不同的二叉搜索树 II
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
from typing import List
from common.treeCommon import *


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        else:
            return self.genTree(1,  n)

    def genTree(self, start, end):
        if start > end:
            return [None]

        trees = []

        for i in range(start, end + 1):
            left_tress = self.genTree(start, i-1)
            right_trees = self.genTree(i+1, end)

            for each_left in left_tress:
                for each_right in right_trees:
                    node = TreeNode(i)
                    node.left = each_left
                    node.right = each_right
                    trees.append(node)
        return trees


s = Solution().generateTrees(1)
a = 1
print(len(s))