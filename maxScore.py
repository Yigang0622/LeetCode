from typing import List

# 1423. 可获得的最大点数
# https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_size = len(cardPoints) - k
        s = sum(cardPoints)
        if window_size == 0:
            return s

        i = 0
        init_window = cardPoints[0:window_size]
        window_sum = sum(init_window)
        points = window_sum

        # 窗口滑动
        while i < len(cardPoints) - window_size:
            window_sum -= cardPoints[i]
            window_sum += cardPoints[i+window_size]
            i += 1
            points = min(points, window_sum)
        return s - points



cardPoints = [1,2,3,4,5,6,1]
k = 3

r = Solution().maxScore(cardPoints, k)
print('ANS',r)