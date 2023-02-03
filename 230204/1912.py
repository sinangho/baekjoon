import sys

n = int(sys.stdin.readline().rstrip())
dp = list(map(int, sys.stdin.readline().rstrip().split()))
sum_list = [0]*n

sum_list[0] = dp[0]

for i in range(1, n):
    sum_list[i] = max(sum_list[i-1]+dp[i], dp[i])
    
print(max(sum_list))