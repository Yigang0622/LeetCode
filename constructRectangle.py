# https://leetcode-cn.com/problems/construct-the-rectangle/

import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        width = int(math.sqrt(area))
        while width > 1:
            if area % width == 0:
                print(width, area/width)
                return [int(area/width), width]
            width -= 1
        return [area, 1]


r = Solution().constructRectangle(3)
print(r)