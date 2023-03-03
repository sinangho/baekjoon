import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    li = deque(li)
    cnt = 0
    while li:
        max_value = max(li)
        front_num = li.popleft()
        M -= 1
        
        if max_value == front_num:
            cnt+=1
            if M < 0:
                print(cnt)
                break
        else:
            li.append(front_num)
            if M < 0:
                M = len(li)-1
        
