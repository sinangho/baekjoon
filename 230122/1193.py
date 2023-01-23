import sys

X = int(sys.stdin.readline().rstrip())

index = 0
start = 0
max = 0
line = -1

if X == 1:
    print("1/1")
    sys.exit(0)

while index != X:
    line+=1
    max+=1
    start = index+1
    index += max
    
    if index >= X:
        break

x좌표 = max-1-(X-start)
y좌표 = max-1-x좌표

분모 = str(x좌표+1)
분자 = str(y좌표+1)


if X > 2 and line % 2 == 0:
    print(분모+'/'+분자)
else:
    print(분자+'/'+분모)

