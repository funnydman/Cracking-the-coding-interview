class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def add(self, x):

        while self.s1:
            self.s2.append(self.s1.pop())

        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):

        if not self.s1:
            raise Exception("Q is Empty")

        return self.s1.pop()


q = Queue()
q.add(1)
q.add(2)
q.add(3)

print(q.pop())
print(q.pop())
print(q.pop())

