import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

miro = []

for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip()))
    miro.append(temp)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1:
                queue.append((nx,ny))
                miro[nx][ny] = miro[x][y] + 1
                
    return miro[N-1][M-1]

print(BFS(0,0))