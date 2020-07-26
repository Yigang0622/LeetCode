# LeetCode
# increasingTriplet 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = float('inf')
        second_min = float('inf')
        for each in nums:
            print(each, first_min, second_min)

            if each < first_min:
                first_min = each
            elif first_min < each < second_min:
                second_min = each
            elif each > first_min and each > second_min:
                return True
        return False


s = Solution().increasingTriplet([1,1,1,1,1,1,1])
print(s)