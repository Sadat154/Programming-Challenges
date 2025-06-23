class MinStack:

    def __init__(self):
        self.stack = []

        self.minVals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minVals:
            self.minVals.append(val)
        else:
            if val < self.minVals[-1]:
                self.minVals.append(val)

    def pop(self) -> None:
        x = self.stack.pop()

        if x == self.minVals[-1]:
            self.minVals.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()