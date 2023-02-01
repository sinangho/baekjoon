import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

DM = set()
BM = set()
output =[]

for i in range(N):
    DM.add(sys.stdin.readline().rstrip())
    
for _ in range(M):
    BM.add(sys.stdin.readline().rstrip())
    
output = list(DM&BM)
        
output.sort()
print(len(output))
for i in output:
    print(i)