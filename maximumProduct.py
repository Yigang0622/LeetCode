# LeetCode
# maximumProduct 
# Created by Yigang Zhou on 2020/8/16.
# Copyright © 2020 Yigang Zhou. All rights reserved.

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 3:
            return 0
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        number_of_neg = 0

        for each in nums:
            if each < 0:
                number_of_neg += 1

        if number_of_neg == 1:
            arr = sorted(nums, reverse=True)
            return arr[0] * arr[1] * arr[2]
        else:
            abs_arr = [abs(x) for x in nums]
            arr = sorted(abs_arr, reverse=True)
            return arr[0] * arr[1] * arr[2]


arr = [1,2,-4,-5,-6]
arr = sorted(arr, reverse=True)
print(arr)

# r = Solution().maximumProduct(arr)
# print(r)