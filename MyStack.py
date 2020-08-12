# 用队列实现栈
# https://leetcode-cn.com/leetbook/read/queue-stack/gw7fg/
import collections

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.deque1 = collections.deque()
        self.deque2 = collections.deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.deque1.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.deque2) == 0:
            while len(self.deque1) > 0:
                self.deque2.append(self.deque1.popleft())
        return self.deque2.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.deque2) == 0:
            while len(self.deque1) > 0:
                self.deque2.append(self.deque1.popleft())
        return self.deque2[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.deque1) == 0 and len(self.deque2) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()