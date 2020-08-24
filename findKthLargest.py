# 数组中的第K个最大元素
# https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvsehe/
from typing import List


class Solution:

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def heapify(self, tree, n, i):
        if i >= n:
            return
        l = i * 2 + 1
        r = i * 2 + 2
        max_i = i
        if l < n and tree[l] > tree[max_i]:
            max_i = l
        if r < n and tree[r] > tree[max_i]:
            max_i = r
        if max_i != i:
            self.swap(tree, i, max_i)
            self.heapify(tree, n, max_i)

    def build_heap(self, arr, n):
        last_node = n - 1
        parent_of_last_node = (last_node - 1) // 2
        for i in range(parent_of_last_node, -1, -1):
            self.heapify(arr, n, i)

    def heap_sort(self, heap, n, kth):
        self.build_heap(heap, n)
        print('Heap:', heap)
        for i in range(n - 1, n - kth - 1, -1):
            self.swap(heap, i, 0)
            print(heap)
            self.heapify(heap, i, 0)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap_sort(nums, len(nums), k)
        return nums[-k]


nums = [3,2,1,5,6,4]
k = 2
r = Solution().findKthLargest(nums, k)
print(r)