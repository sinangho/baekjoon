import sys

N = int(sys.stdin.readline().rstrip())
stairs = [0]*(N+2)
score = [0]*(N+2)

for i in range(1, N+1):
    stairs[i] = int(sys.stdin.readline().rstrip())
    
score[1] = stairs[1]
score[2] = stairs[1]+stairs[2]

for i in range(3, N+1):
    score[i] = max(stairs[i]+stairs[i-1]+score[i-3], stairs[i]+score[i-2])
    
print(score[N])

