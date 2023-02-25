import sys
from collections import deque

L_str = list(sys.stdin.readline().rstrip())
R_str = []
M = int(sys.stdin.readline().rstrip())

for _ in range(M):
    cmd = list(sys.stdin.readline().rstrip())
    
    if cmd[0] == "L":
        if L_str:
            R_str.append(L_str.pop())
    elif cmd[0] == "D":
        if R_str:
            L_str.append(R_str.pop())
    elif cmd[0] == "B":
        if L_str:
            L_str.pop()
    else:
        L_str.append(cmd[2])

R_str.reverse()
answer = L_str+R_str
for i in answer:
    print(i,end="")