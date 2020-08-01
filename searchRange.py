from typing import List

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/50/sorting-and-searching/100/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx = self.bin_search(nums, target)
        if idx == -1:
            return [-1,-1]

        print('index', idx)
        start = idx
        end = idx

        while start >= 1 and nums[start - 1] == target:
            start -= 1

        while end+1 < len(nums) and nums[end+1] == target:
            end += 1

        return [start, end]



    def bin_search(self, nums, target):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print(mid, left,right)

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1



nums = [1,1,1]
target = 1
r = Solution().searchRange(nums, target)
print(r)