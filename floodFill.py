# 图像渲染
# https://leetcode-cn.com/leetbook/read/queue-stack/g02cj/

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        h = len(image)
        if h == 0:
            return image
        w = len(image[0])
        baseColor = image[sr][sc]
        if newColor == baseColor:
            return image
        self.mark(image, sr, sc, newColor, baseColor, w, h)
        return image

    def mark(self, image, sr, sc, newColor, baseColor, w, h):
        if sr < 0 or sr >= h or sc < 0 or sc >= w:
            return
        if image[sr][sc] != baseColor:
            return
        image[sr][sc] = newColor
        self.mark(image, sr + 1, sc, newColor, baseColor, w, h)
        self.mark(image, sr - 1, sc, newColor, baseColor, w, h)
        self.mark(image, sr, sc + 1, newColor, baseColor, w, h)
        self.mark(image, sr, sc - 1, newColor, baseColor, w, h)

image = [[0,0,0],
         [0,1,1]]
sr = 1
sc = 1
newColor = 1
r = Solution().floodFill(image, sr, sc, newColor)
print(r)
