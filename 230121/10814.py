import sys

N = int(sys.stdin.readline().rstrip())

info = []
    
for _ in range(N):
    temp=[]
    a, b = map(str, sys.stdin.readline().rstrip().split())
    temp.append(int(a))
    temp.append(b)
    info.append(temp)
    
    
info.sort(key=lambda x: x[0])

for i in range(N):
    print(info[i][0], info[i][1])
    