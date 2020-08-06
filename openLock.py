# 打开转盘锁
#
from typing import List
import collections

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        seen = {'0000'}
        q = collections.deque([('0000', 0)])

        while q:
            node, depth = q.popleft()
            if node == target:
                return depth
            if node not in deadends:
                for each in self.next(node):
                    if each not in seen:
                        seen.add(each)
                        q.append((each, depth+1))
        return -1

    def next(self, current):
        results = []
        for i in range(len(current)):
            digit = int(current[i])
            for j in (-1, 1):
                new_digit = (digit + j) % 10
                new = current[:i] + str(new_digit) + current[i+1:]
                results.append(new)
        return results



deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
r = Solution().openLock(deadends, target)
print(r)