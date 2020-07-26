# LeetCode
# MedianFinder 
# Created by Yigang Zhou on 2020/7/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.

class MedianFinder:

    arr = []
    median = 0

    def __init__(self):
        """
        initialize your data structure here.
        """

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        if len(self.arr) %2 == 0:
            self.median = (self.median*2 + num) / 2

    def findMedian(self) -> float:
        print(self.median)
        return self.median

m = MedianFinder()

m.addNum(1)
m.addNum(2)
m.findMedian()
m.addNum(3)
m.findMedian()


