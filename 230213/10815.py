import sys

N = int(sys.stdin.readline().rstrip())
A_set = set(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
B_set = list(map(int, sys.stdin.readline().rstrip().split()))

intersection = A_set & set(B_set)

for i in B_set:
    if i in intersection:
        print(1, end=" ")
    else:
        print(0, end=" ")