# LeetCode
# convert 
# Created by Yigang Zhou on 2020/9/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 6. Z 字形变换
# https://leetcode-cn.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        dir = 'd'
        i = 0
        arrs = [[] for _ in range(numRows)]

        for c in s:
            if dir == 'd':
                print(c)
                arrs[i].append(c)
                i += 1
                if i == numRows:
                    i -= 2
                    dir = 'u'
            elif dir == 'u':
                arrs[i].append(c)
                i -= 1
                if i == -1:
                    i = 1
                    dir = 'd'
        print(arrs)

        return ''.join([''.join(x) for x in arrs])




s = "LEETCODEISHIRING"
numRows = 3
s = Solution().convert(s, numRows)
print(s)