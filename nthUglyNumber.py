# https://leetcode-cn.com/problems/chou-shu-lcof/
# 剑指 Offer 49. 丑数
import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = []
        seen = set()

        heap = []
        heapq.heappush(heap, 1)

        while len(ugly_nums) < n:
            num = heapq.heappop(heap)
            ugly_nums.append(num)
            for factor in [2,3,5]:
                ugly_num = num * factor
                if ugly_num not in seen:
                    seen.add(ugly_num)
                    heapq.heappush(heap, ugly_num)

        return ugly_nums[-1]

r = Solution().nthUglyNumber(10)
print(r)
