import sys

n = int(sys.stdin.readline().rstrip())
wine = [0]*n
dp = [0]*n

for i in range(n):
    wine[i] = int(sys.stdin.readline().rstrip())

dp[0] = wine[0]

if n > 1:
    dp[1] = wine[0]+wine[1]

if n > 2:
    dp[2] = max(dp[1], wine[1]+wine[2], wine[0]+wine[2])

for i in range(3, n):
    dp[i] = max(wine[i] + dp[i-2], wine[i-1]+dp[i-3]+wine[i], dp[i-1])
    
print(dp[n-1])