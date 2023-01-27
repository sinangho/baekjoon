import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

number_list = deque(list(map(int, sys.stdin.readline().rstrip().split())))
sum=0
sumlist = deque([0])

for i in number_list:
    sum += i
    sumlist.append(sum)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(sumlist[j] - sumlist[i-1])