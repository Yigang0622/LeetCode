# LeetCode
# corpFlightBookings 
# Created by Yigang Zhou on 2020/9/6.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 航班预订统计
# https://leetcode-cn.com/problems/corporate-flight-bookings/
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0] * n
        for each in bookings:
            i,j,k = each[0], each[1], each[2]
            for x in range(i-1,j):
                seats[x] += k
        return seats

bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
n = 5
s = Solution().corpFlightBookings(bookings,n)