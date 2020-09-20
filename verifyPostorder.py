# LeetCode
# verifyPostorder 
# Created by Yigang Zhou on 2020/9/20.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 剑指 Offer 33. 二叉搜索树的后序遍历序列
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        print(postorder)
        return self.verify(postorder, 0, len(postorder) - 1)

    def verify(self, postorder, i, j):
        if i >= j:
            return True
        parent = postorder[j]
        print(postorder[i:j + 1], 'parent is', parent)
        m = i
        while postorder[m] < parent:
            m += 1
        temp = m
        while temp < j:
            if postorder[temp] < parent:
                return False
            temp += 1


        return self.verify(postorder, i, m-1) and self.verify(postorder, m, j - 1)


postorder = [4,6,7,5]
r = Solution().verifyPostorder(postorder)
print(r)
