# LeetCode
# QuickSort 
# Created by Yigang Zhou on 2020/8/21.
# Copyright © 2020 Yigang Zhou. All rights reserved.

class QuickSort:

    def sort(self, nums):
        print(nums)
        self.quick_sort(nums,0,len(nums)-1)
        print(nums)

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def quick_sort(self, nums, start, end):
        if start >= end:
            return

        pivot = start
        i = start
        j = end
        pivot_val = nums[pivot]
        while i < j:

            while i < j and nums[j] > pivot_val:
                j -= 1

            while i < j and nums[i] <= pivot_val:
                i += 1
            self.swap(nums, i, j)
        self.swap(nums,pivot,i)

        self.quick_sort(nums, start, i - 1)
        self.quick_sort(nums, i + 1, end)


nums = [12,3,4,5,6,7,8]
s = QuickSort().sort(nums)
