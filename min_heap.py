# LeetCode
# min_heap 
# Created by Yigang Zhou on 2020/8/20.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 小顶堆

class MinHeap:

    def heapify(self, tree, n, i):
        if i >= n:
            return
        l = i * 2 + 1
        r = i * 2 + 2
        min_node = i
        if l < n and tree[l] < tree[min_node]:
            min_node = l
        if r < n and tree[r] < tree[min_node]:
            min_node = r
        if i != min_node:
            self.swap(tree,i,min_node)
            self.heapify(tree,n,min_node)

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

    def solve(self, arr):
        print(arr)
        self.heap_sort(arr)
        print(arr)



nums = [9,1,4,6,2,4,8,3,0]
s = MinHeap().solve(nums)
