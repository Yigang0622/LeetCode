# LeetCode
# isValidSerialization 
# Created by Yigang Zhou on 2020/11/8.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 331. 验证二叉树的前序序列化
# https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder_list = preorder.split(',')

        num_of_hash = 0
        while preorder_list:
            e = preorder_list.pop()
            if e == '#':
                num_of_hash += 1
            else: #数字
                if num_of_hash >= 2:
                    preorder_list.append('#')
                    num_of_hash -= 2
                else:
                    # print("不行!")
                    return False
            # print(preorder_list)
        # print(num_of_hash)
        return num_of_hash == 1

preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
s = Solution().isValidSerialization(preorder)
