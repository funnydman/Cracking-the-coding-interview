"""
Task:
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
Notes:
possible solutions: having node with min, putting min on the stack consistently.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        if not self.min:
            self.min.append(x)
        else:
            if x < self.stack[-1]:
                self.min.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        elem = self.stack.pop()
        if elem == self.min[-1]:
            self.min.pop()
        return elem

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min[-1]


stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-1)
stack.get_min()  # 1
