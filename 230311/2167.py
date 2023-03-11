N, M = map(int, input().split())

ls = []

for i in range(N):
    ls.append(list(map(int, input().split())))
    
K = int(input())

coordinate = []

for i in range(K):
    coordinate.append(list(map(int, input().split())))
    
# for i in range(K):