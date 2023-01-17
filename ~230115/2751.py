import sys

N = int(sys.stdin.readline().rstrip())

temp = []
cnt=0
for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    temp.append(num)

temp.sort()

for i in temp:
    print(i)