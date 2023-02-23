import sys

def bs(li, n):
    start, end = 0, len(li)-1
    res = 0
    while start <= end:
        m = (start+end)//2
        if int(li[m][1]) >= n:
            end = m-1
            res = m
        else:
            start = m+1
    return res

N, M = map(int, sys.stdin.readline().split())
li = [sys.stdin.readline().split() for _ in range(N)]
for _ in range(M):
    n = int(sys.stdin.readline())
    print(li[bs(li, n)][0])