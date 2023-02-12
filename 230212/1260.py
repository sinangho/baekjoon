import sys
from collections import deque
import heapq

N, M, V = map(int, sys.stdin.readline().rstrip().split())

graph = [[0]*(N+1) for i in range(N+1)]
visited = [0]*(N+1)
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = graph[b][a] = 1

# DFS
def dfs(v):
    if visited[v] == 0:
        visited[v] = 1
        print(v, end=" ")
        for i in range(1, N+1):
            if graph[v][i] == 1:
                dfs(i)
dfs(V)
print()
# BFS
visited[V] = 0
dq = deque([V])
while dq:
    current = dq.popleft()
    print(current, end=" ")
    for i in range(1, N+1):
        if visited[i] == 1 and graph[current][i] == 1:
            dq.append(i)
            visited[i] = 0
            
