import sys

N = int(sys.stdin.readline().rstrip())

info = []
rank = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    info.append(temp)
    
for i in info:
    w = i[0]
    h = i[1]
    cnt = 1
    for j in info:
        if w < j[0] and h < j[1]:
            cnt += 1
    rank.append(cnt)

for i in rank:
    print(i, end=" ")

