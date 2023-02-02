import sys 

N = int(sys.stdin.readline().rstrip())
RGB = [[0 for j in range(3)] for i in range(N+1)]
cost = [0]*3

for i in range(1,N+1):
    cost[0], cost[1], cost[2] = map(int, sys.stdin.readline().rstrip().split())
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + cost[0]
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + cost[1]
    RGB[i][2] = min(RGB[i-1][1], RGB[i-1][0]) + cost[2]
    
print(min(RGB[N][2], RGB[N][0], RGB[N][1]))


