# LeetCode
# titleToNumber 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# https://leetcode-cn.com/explore/interview/card/top-interview-questions/268/hash-map/1162/

class Solution:
    def titleToNumber(self, s: str) -> int:
        arr = []
        multipler = 26
        for each in s:
            arr.append(self.charToNumber(each))

        sum = 0
        for i in range(len(arr)):
            sum += arr[i] * pow(multipler, len(arr) - i - 1)
        return sum

    def charToNumber(self, char) -> int:
        return ord(char) - 64

s = Solution().titleToNumber('ZY')