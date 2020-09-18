# LeetCode
# MaxQueue 
# Created by Yigang Zhou on 2020/9/17.
# Copyright © 2020 Yigang Zhou. All rights reserved.
import collections

class MaxQueue:

    def __init__(self):
        self.q = collections.deque()
        self.q_max = collections.deque()

    def max_value(self) -> int:
        if self.q_max:
            return self.q_max[0]
        return -1

    def push_back(self, value: int) -> None:
        self.q.append(value)
        while self.q_max and self.q_max[-1] < value:
            self.q_max.pop()
        self.q_max.append(value)

    def pop_front(self) -> int:
        if not self.q:
            return -1
        e = self.q.popleft()
        if self.q_max and self.q_max[0] == e:
            self.q_max.popleft()
        return e


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()