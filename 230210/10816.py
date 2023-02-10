import sys
 
N = int(sys.stdin.readline().rstrip())

num_list = list(map(int, sys.stdin.readline().rstrip().split()))
num_hash = {}

M = int(sys.stdin.readline().rstrip())
mycard = list(map(int, sys.stdin.readline().rstrip().split()))

num_hash[str(num_list[0])] = 1

for i in range(1, N):
    cnt = num_hash.get(str(num_list[i]), 0)
    if cnt == 0:
        num_hash[str(num_list[i])] = 1
    else:
        num_hash[str(num_list[i])] += 1
        
for i in range(0, M):
    print(num_hash.get(str(mycard[i]), 0),end=" ")
    