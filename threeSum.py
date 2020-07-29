# LeetCode
# threeSun 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        length = len(nums)
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    if i != j != k and nums[i] + nums[j] + nums[k] == 0:
                        s = {nums[i], nums[j], nums[k]}
                        ans.add(s)
        print(ans)

Solution().threeSum([-1, 0, 1, 2, -1, -4])


