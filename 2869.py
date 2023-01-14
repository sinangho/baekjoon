import sys

A, B, V = map(int, sys.stdin.readline().rstrip().split())

temp = V-A
cnt = 0

if A-B > temp:
    cnt = temp%(A-B)
    cnt += 1
    
    
else:
    if temp%(A-B) != 0:
        cnt = temp//(A-B) + 2
    else:
        cnt = temp//(A-B) + 1
    
print(cnt)