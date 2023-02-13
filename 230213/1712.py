import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())

if C-B == 0:
    print(-1)

else:
    sonic = A//(C-B) + 1

    if sonic < 0:
        sonic = -1
        
    print(sonic)