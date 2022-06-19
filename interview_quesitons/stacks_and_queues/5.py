stack = [2, 7, 1, 10, 3]

tmp_stack = []

while stack:
    temp = stack.pop()
    while tmp_stack and tmp_stack[-1] > temp:
        stack.append(tmp_stack.pop())
    tmp_stack.append(temp)
    
    
def sort_stack(stack):
    result = []
    while stack:
        elem = stack.pop()
        temp = []
        while result and elem >= result[-1]:
            temp.append(result.pop())
        result.append(elem)
        while temp:
            result.append(temp.pop())
    return result

print(sort_stack(stack))
