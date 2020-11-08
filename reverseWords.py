# LeetCode
# reverseWords 
# Created by Yigang Zhou on 2020/11/7.
# Copyright © 2020 Yigang Zhou. All rights reserved.
import collections
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(' ')
        d = collections.deque()

        for each in words:
            if each != '':
                d.appendleft(each.strip())

        return ' '.join(d)



s = "a good   example"
r = Solution().reverseWords(s)
print(r)