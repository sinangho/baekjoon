import sys

N = sys.stdin.readline().rstrip()
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
max_num = max(num_list)
prime = [1]*(max_num+1)
prime[0],prime[1] = 0,0
cnt = 0

for i in range(2, int(max_num**0.5)+1):
    if prime[i] == 1:
        for j in range(i*2, max_num+1, i):
            prime[j] = 0

for i in num_list:
    if prime[i] == 1:
        cnt += 1
        
print(cnt)