import sys

N = int(sys.stdin.readline().rstrip())

N_list = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline().rstrip())

M_list = list(map(int, sys.stdin.readline().rstrip().split()))

N_list.sort()

for i in M_list:
    left, right = 0, N-1
    flag = False
    
    while left <= right:
        center = (left+right)//2
        if i == N_list[center]:
            print(1)
            flag = True
            break
        elif i > N_list[center]:
            left = center+1
        else:
            right = center-1
            
    if not flag:
        print(0)