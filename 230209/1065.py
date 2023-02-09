import sys

N = int(sys.stdin.readline().rstrip())

if N < 100:
    print(N)
else:
    for i in range(100, N+1):
        temp = str(i)
        num = []
        for j in temp:
            num.append(int(j))
        
        d = num[1] - num[0]    
        for i in range(1, len(num)-1):
            if num[i+1] - num[i] != d:
                N-=1
                break
    print(N)