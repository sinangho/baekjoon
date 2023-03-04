import sys

N = int(sys.stdin.readline().rstrip())
coordinate = []

for i in range(N):
    xy = list(map(int, sys.stdin.readline().rstrip().split()))
    coordinate.append(xy)
    
coordinate.sort(key=lambda x : (x[1], x[0]))

for i in range(N):
    print(coordinate[i][0], coordinate[i][1])