import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    
    dp = [[i for i in range(1,n+1)]for j in range(k+2)]
    
    for i in range(1, k+1):
        for j in range(1, n):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
            
    print(dp[k][n-1])