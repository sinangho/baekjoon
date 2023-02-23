import sys

def BS(li, power):
    start, end = 0, len(li)-1
    res = 0
    while start<=end:
        mid = (start+end)//2
        if int(li[mid][1]) >= power:
            res = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return res

answer = []
N, M = map(int, sys.stdin.readline().rstrip().split())
li = [sys.stdin.readline().rstrip().split() for _ in range(N)]

for _ in range(M):
    power = int(sys.stdin.readline().rstrip())
    answer.append(li[BS(li,power)][0])

for i in answer:
    print(i)