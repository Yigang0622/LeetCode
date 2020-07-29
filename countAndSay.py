# LeetCode
# countAndSay 
# Created by Yigang Zhou on 2020/7/21.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            r = '1'
            for i in range(n-1):
                r = self.say(r)
            return r

    def say(self, s: str):
        last = -1
        number = []
        count = []
        for each in s:
            if each != last:
                number.append(each)
                count.append(1)
                last = each
            else:
                count[len(count)-1] += 1
        r = ''
        for i in range(len(number)):
            r += str(count[i]) + number[i]
        return r

r = Solution().countAndSay(4)
print(r)