# LeetCode
# StackOfPlates 
# Created by Yigang Zhou on 2020/10/7.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 面试题 03.03. 堆盘子
# https://leetcode-cn.com/problems/stack-of-plates-lcci/

class StackOfPlates:

    def __init__(self, cap: int):
        self.max_cap = cap
        self.stacks = []


    def push(self, val: int) -> None:
        if self.max_cap == 0:
            return
        if not len(self.stacks):
            self.stacks.append([])
        if len(self.stacks[-1]) == self.max_cap:
            self.stacks.append([])
        self.stacks[-1].append(val)


    def pop(self) -> int:
        if self.max_cap == 0:
            return -1
        if not len(self.stacks) or not len(self.stacks[-1]):
            return -1
        e = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return e

    def popAt(self, index: int) -> int:
        if self.max_cap == 0:
            return -1
        if index > len(self.stacks) - 1:
            return -1
        if not len(self.stacks[index]):
            return -1
        e = self.stacks[index].pop()
        if len(self.stacks[index]) == 0:
            del self.stacks[index]
        return e


# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)