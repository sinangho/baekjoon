import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
visited = [0]*10001

def BFS(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == K:
            return visited[v]
        for i in (v-1, v+1, v*2):
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = visited[v] + 1
                q.append(i)
                
print(BFS(N))