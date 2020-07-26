# LeetCode
# intersect 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# https://leetcode-cn.com/explore/interview/card/top-interview-questions/264/array/1132/
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        count2 = {}
        arr = nums1
        arr2 = nums2
        if len(nums2) < len(nums1):
            arr = nums2
            arr2 = nums1

        for each in arr:
            if each in count:
                count[each] += 1
            else:
                count[each] = 1

        for each in arr2:
            if each in count and count[each] >= 1:

                if count[each] == 1:
                    count[each] = -1
                else:
                    count[each] -= 1

                if each in count2:
                    count2[each] += 1
                else:
                    count2[each] = 1

        result = []
        for each in count2:
            for i in range(count2[each]):
                result.append(each)
        print(result)
        return result

r = Solution().intersect([1,2,2,1],[2,2])

