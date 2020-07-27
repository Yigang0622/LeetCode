class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.stack = []
        self.min =0

    def push(self, x: int) -> None:
        self.stack.append(x)

        if len(self.stack) == 0:
            self.stack.append(x)
            self.min_stack.append(x)
            self.min = x
            return

        if x < self.min:
            self.min = x
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return 0
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return 0
        return self.min_stack[len(self.min_stack) - 1]


obj = MinStack()
obj.push(-1)
obj.push(2)
obj.push(-5)
obj.push(4)
obj.pop()
obj.pop()
obj.pop()
obj.pop()

print(obj.top())
print(obj.getMin())