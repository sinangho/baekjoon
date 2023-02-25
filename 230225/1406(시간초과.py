import sys
from collections import deque

N = list(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

index = len(N)

for _ in range(M):
    cmd = list(sys.stdin.readline().rstrip())
    
    if cmd[0] == "L":
        index -= 1
    elif cmd[0] == "D":
        index += 1
    elif cmd[0] == "B":
        if index == 0:
            continue
        else:
            del N[index-1]
            index-=1
    else:
        if index == len(N):
            N.append(cmd[2])
            index+=1
        else:
            N.insert(index, cmd[2])
    
    if index < 0:
        index = 0
    elif index > len(N):
        index = len(N)
    
for i in N:
    print(i,end="")