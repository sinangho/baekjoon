import sys

N = int(sys.stdin.readline().rstrip())

calc_list = [0]*(N+1)

for i in range(2, N+1):
    
    calc_list[i] = calc_list[i-1]+1
    
    if i%3==0:
        calc_list[i] = min(calc_list[i], calc_list[i//3]+1)
    if i%2==0:
        calc_list[i] = min(calc_list[i], calc_list[i//2]+1)
        
print(calc_list[N])