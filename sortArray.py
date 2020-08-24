# LeetCode
# sortArray 
# Created by Yigang Zhou on 2020/8/20.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# https://leetcode-cn.com/problems/sort-an-array/
from typing import List


class Solution:


    def heapify(self, tree, n, i):
        if i >= n:
            return
        l = i * 2 + 1
        r = i * 2 + 2
        max_node = i
        if l < n and tree[l] > tree[max_node]:
            max_node = l
        if r < n and tree[r] > tree[max_node]:
            max_node = r
        if i != max_node:
            self.swap(tree,i,max_node)
            self.heapify(tree,n,max_node)

    def build_heap(self, arr, n):
        last_node = n - 1
        parent = (last_node - 1)//2
        for i in range(parent, -1, -1):
            self.heapify(arr, n, i)

    def heap_sort(self, arr):
        n = len(arr)
        self.build_heap(arr, n)
        for i in range(n - 1, -1 , -1):
            self.swap(arr,0,i)
            self.heapify(arr,i,0)

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def sortArray(self, nums: List[int]) -> List[int]:
        self.heap_sort(nums)
        return nums

arr = [1,5,7,3,2,1,4,55,3]
r= Solution().sortArray(arr)
print(r)

