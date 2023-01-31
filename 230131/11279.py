import heapq
import sys
N = int(input())
dp = []

for _ in range(N):
    cmd = int(sys.stdin.readline().rstrip())
    
    if cmd == 0:
        if dp:
            print(heapq.heappop(dp)*(-1))
        else:
            print(0)
    else:
        heapq.heappush(dp, (-1)*cmd)