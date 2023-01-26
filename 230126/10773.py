from collections import deque
K = int(input())
stack = deque()

for _ in range(K):
    num = int(input())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()
        
print(sum(stack))
    