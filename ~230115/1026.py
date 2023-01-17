import sys

N = int(sys.stdin.readline().rstrip())

A_list = list(map(int, sys.stdin.readline().rstrip().split()))
B_list = list(map(int, sys.stdin.readline().rstrip().split()))

sum = 0
A_list.sort()
B_list.sort(reverse=True)

for i in range(N):
    sum += A_list[i] * B_list[i]
    
print(sum)