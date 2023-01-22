import sys

N = int(sys.stdin.readline().rstrip())
coordinates = []

for _ in range(N):
   coordinates.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
coordinates.sort(key=lambda x:(x[0], x[1]))

for i in coordinates:
    print(i[0], i[1])