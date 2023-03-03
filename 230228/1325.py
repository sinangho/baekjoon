import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

visited = [0]*(N+1)
graph = [[] for _ in range(N+1)]

def BFS(v):
    queue = deque([v])
    visited = [False] * (N+1)
    visited[v] = True
    cnt = 1
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt+=1
    
    return cnt

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[b].append(a)
    
answer = []
max = -1

for i in range(1, N+1):
    result = BFS(i)
    if result > max:
        answer = [i]
        max = result
    elif result == max:
        answer.append(i)
        
for i in answer:
    print(i, end=" ")