from typing import List

# 剑指 Offer 66. 构建乘积数组
# https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        N = len(a)
        arr1 = [1] * N
        arr2 = [1] * N
        for i in range(1, N):
            arr1[i] = arr1[i - 1] * a[i - 1]
            j = N - i - 1
            arr2[j] = arr2[j + 1] * a[j + 1]
            # print(arr1)
            # print(arr2)
        # print(arr1)
        # print(arr2)
        return [arr1[x] * arr2[x] for x in range(N)]




a = [1,2,3,4,5]
r = Solution().constructArr(a)
print(r)