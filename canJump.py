from typing import List
from common.arrayCommon import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        print(nums)
        print2DArray(dp)
        for i in range(n):
            for j in range(i):
                dp[i][j] = j - i == nums[i]
        print2DArray(dp)


arr = [2,3,1,1,4]
r = Solution().canJump(arr)