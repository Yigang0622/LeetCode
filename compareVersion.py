# LeetCode
# compareVersion 
# Created by Yigang Zhou on 2020/9/10.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 比较版本号
# https://leetcode-cn.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_arr = version1.split('.')
        version2_arr = version2.split('.')
        n_v1 = len(version1_arr)
        n_v2 = len(version2_arr)
        n = max(n_v1, n_v2)
        for i in range(n):
            v1 = 0
            v2 = 0
            if i < n_v1:
                v1 = int(version1_arr[i])
            if i < n_v2:
                v2 = int(version2_arr[i])
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        return 0

version1 = "1"
version2 = "0"
r = Solution().compareVersion(version1, version2)
print(r)