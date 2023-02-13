import sys

N = int(sys.stdin.readline().rstrip())

def fact(n):
    if n > 1:
        return n*fact(n-1)
    else:
        return 1
    
str_num = str(fact(N))
cnt = 0
for i in range(len(str_num)-1, -1, -1):
    if str_num[i] == '0':
        cnt += 1
    else:
        print(cnt)
        break