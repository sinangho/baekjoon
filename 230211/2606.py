import sys
from collections import deque

pc = int(sys.stdin.readline().rstrip())
connect = int(sys.stdin.readline().rstrip())

graph = [[] for i in range(pc+1)]
visited = [0]*(pc+1)

for i in range(connect):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    graph[n]+=[m]
    graph[m]+=[n]
    
# visited[1] = 1
# dq = deque([1])

# while dq:
#     current_pc = dq.popleft()
    
#     for i in graph[current_pc]:
#         if visited[i] == 0:
#             dq.append(i)
#             visited[i] = 1
            
# print(sum(visited)-1)
def dfs(index):
    visited[index] = 1
    for i in graph[index]:
        if visited[i] == 0:
            dfs(i)
            
dfs(1)
print(sum(visited)-1)