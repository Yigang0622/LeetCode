# LeetCode
# threeSun 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        print(nums)
        self.search([],nums,ans)
        for each in ans:
            print(each)

    def search(self, current, possible_choice, ans):
        if len(current) == 3:
            if sum(current) == 0:
                ans.append(current)
        else:
            for each in possible_choice:
                a = current[:]
                a.append(each)
                b = possible_choice[:]
                b.remove(each)
                self.search(a, b, ans)

Solution().threeSum([-1, 0, 1, 2, -1, -4])


