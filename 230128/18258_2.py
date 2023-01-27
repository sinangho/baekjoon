import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

que = deque()

for _ in range(N):
    i = deque(list(map(str, sys.stdin.readline().rstrip().split())))
    
    if i[0] == "push":
        que.append(i[1])
    elif i[0] == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif i[0] == "size":
        print(len(que))
    elif i[0] == 'empty' and que:
        print(0)
    elif i[0] == 'empty' and not que:
        print(1)
    elif i[0] == 'front' and que:
        obj = que.popleft()
        que.appendleft(obj)
        print(obj)
    elif i[0] == 'back' and que:
        obj = que.pop()
        que.append(obj)
        print(obj)
    else:
        print(-1)
    
    
