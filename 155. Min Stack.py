class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curr_min = self.getMin()
        if curr_min is None or val < curr_min:
            curr_min = val
        self.stack.append((val, curr_min))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()