# LeetCode
# partitionLabels 
# Created by Yigang Zhou on 2020/10/22.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 763. 划分字母区间
# https://leetcode-cn.com/problems/partition-labels/
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_index = dict()
        for i, c in enumerate(S):
            last_index[c] = i
        # print(last_index)
        start = 0
        end = 0
        ans = []
        for i, c in enumerate(S):
            end = max(end, last_index[c])
            if i == end:
                # print(S[start:end])
                ans.append(end + 1 - start)
                start = end + 1
        # print(ans)
        return ans

S = "ababcbacadefegdehijhklij"
s = Solution().partitionLabels(S)
print(s)