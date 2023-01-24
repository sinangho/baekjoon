import sys

n = int(sys.stdin.readline().rstrip())

Fibo = [0]*91

Fibo[0] = 0
Fibo[1] = 1
Fibo[2] = 1

for i in range(3, n+1):
    Fibo[i] = Fibo[i-1]+Fibo[i-2]
    
print(Fibo[n])