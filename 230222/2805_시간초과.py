import heapq
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
temp = list(map(int, sys.stdin.readline().rstrip().split()))
tree = []

for i in temp:
    heapq.heappush(tree, i*(-1))

for i in range(M):
    max = heapq.heappop(tree)
    max += 1
    heapq.heappush(tree, max)
    
print(heapq.heappop(tree)*(-1))