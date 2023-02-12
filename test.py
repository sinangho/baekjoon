import sys
from collections import deque

N,M,V = map(int, sys.stdin.readline().split())
a_list = [[False]*(N+1)for i in range(N+1)] 
visited = [False]*(N+1)


for i in range(M):
    a, b =  map(int,sys.stdin.readline().split())
    a_list[a][b] = a_list[b][a] = True

print(a_list)