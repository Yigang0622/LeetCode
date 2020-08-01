# 合并区间
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/50/sorting-and-searching/101/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        print(intervals)
        ans = []
        for each in intervals:
            if not ans or ans[-1][1] < each[0]:
                ans.append(each)
            else:
                ans[-1] = [ans[-1][0], max(ans[-1][1], each[1])]
        return ans




intervals = [[1,3],[2,6],[8,10],[15,18]]
r = Solution().merge(intervals)
print(r)