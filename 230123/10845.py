import sys

N = int(sys.stdin.readline().rstrip())

command = []
que = []

for _ in range(N):
    temp = list(map(str, sys.stdin.readline().rstrip().split()))
    command.append(temp)
    
for i in command:
    
    if len(i) == 2:
        cmd = i[0]
        num = i[1]
    else:
        cmd = i[0]
        
    if cmd == "push":
        que.append(num)
    elif cmd == "pop":
        if que:
            print(que[0])
            del que[0]
        else:
            print(-1)
    elif cmd == "size":
        print(len(que))
    elif cmd == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif cmd == 'back':
        if que:
            a = que.pop()
            print(a)
            que.append(a)
        else:
            print(-1)