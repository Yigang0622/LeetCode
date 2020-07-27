from typing import List


def binSearch(arr:List[int], target:int) -> int:
    left = 0
    right = len(arr) - 1
    mid = int((right - left)/2)

    while left < right:
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid
        elif arr[mid] > target:
            right = mid
        mid = int((right - left)/2)
        print(left, right)
    return -1

arr = [1,2,3]
r = binSearch(arr, 2)
print(r)
