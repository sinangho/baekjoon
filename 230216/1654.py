import sys
import math

N, K = map(int, sys.stdin.readline().rstrip().split())

LAN = []

for i in range(N):
    LAN.append(int(sys.stdin.readline().rstrip()))
    
max = max(LAN)
min = 1

while min <= max:
    mid = (max+min)//2
    cnt = 0
    
    for i in LAN:
        cnt += i//mid
        
    if cnt >= K:
        min = mid+1
    else:
        max = mid-1
            
print(max)