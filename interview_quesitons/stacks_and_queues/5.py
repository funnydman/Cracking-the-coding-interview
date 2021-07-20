stack = [2, 7, 1, 10, 3]

tmp_stack = []

while stack:
    temp = stack.pop()
    while tmp_stack and tmp_stack[-1] > temp:
        stack.append(tmp_stack.pop())
    tmp_stack.append(temp)

print(tmp_stack)
