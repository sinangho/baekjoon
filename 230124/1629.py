import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())

def f(A, B, C):
    if B == 1:
        temp = A%C
        return temp
    
    temp = f(A, B//2, C)
    if B % 2 == 0:
        return temp*temp%C
    else:
        return temp*temp*A%C
    
print(f(A,B,C))