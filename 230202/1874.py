import sys

n = int(sys.stdin.readline().rstrip())

dp = []
output = []
cnt = 1
flag = True

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    
    while cnt <= num:
        dp.append(cnt)
        output.append("+")
        cnt+=1
    
    if dp[-1] == num:
        dp.pop()
        output.append("-")
    
    else:
        flag = False

if flag:
    for i in output:
        print(i)
else:
    print("NO")
