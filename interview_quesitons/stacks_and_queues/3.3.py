class StackOfPlates:
    def __init__(self, capacity):
        self.capacity = capacity
        self._stack = [[]]
        self.curr = 0

    def push(self, x):
        if len(self._stack[self.curr]) == self.capacity:
            self.curr += 1
            self._stack.append([])

        self._stack[self.curr].append(x)

    def pop(self):
        while not self._stack[self.curr] and self.curr >= 0:
            self.curr -= 1

        if not self._stack[self.curr]:
            raise Exception('stack is empty')

        self._stack[self.curr].pop()


stack = StackOfPlates(2)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.pop()
stack.pop()

stack.pop()

stack.pop()

stack.pop()

print(stack._stack)
