import sys

N = int(sys.stdin.readline().rstrip())

N_list = set(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline().rstrip())

M_list = list(map(int, sys.stdin.readline().rstrip().split()))

for i in M_list:
    if i in N_list:
        print(1)
    else:
        print(0)