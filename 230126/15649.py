from itertools import permutations

N, M = map(int, input().split())
num = []
for i in range(1, N+1):
    num.append(i)
    
for i in permutations(num, r=M):
    temp = list(i)
    for j in temp:
        print(j)