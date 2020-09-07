# 前k个高频元素
# https://leetcode-cn.com/problems/top-k-frequent-elements/
from typing import List


class Solution:

    numbers = []

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

        temp = self.numbers[i]
        self.numbers[i] = self.numbers[j]
        self.numbers[j] = temp

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

    def heap_sort(self, heap, n, k):
        self.build_heap(heap, n)
        print('Heap:', heap)
        for i in range(n - 1, n - k - 1, -1):
            self.swap(heap, i, 0)
            print(heap)
            self.heapify(heap, i, 0)


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for each in nums:
            if each in count_dict:
                count_dict[each] += 1
            else:
                count_dict[each] = 1
        frequency = []
        numbers = []
        for e in count_dict:
            numbers.append(e)
            frequency.append(count_dict[e])
        N = len(numbers)
        self.numbers = numbers
        self.heap_sort(frequency, N, k)
        return self.numbers[N-k:][::-1]





nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4]
k = 3
r = Solution().topKFrequent(nums, k)
print('1',r)