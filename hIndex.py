from typing import List


# 274. H 指数
# https://leetcode-cn.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        # print(citations)
        i = 0
        while i < n and i + 1 <= citations[i]:
            print()
            i += 1

        return i



citations = [3, 0, 6, 1, 5]
r = Solution().hIndex(citations)
print(r)