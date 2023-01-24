import sys

N = int(sys.stdin.readline().rstrip())

waiting_time = list(map(int, sys.stdin.readline().rstrip().split()))
total_time = [0]    
waiting_time.sort()

for i in range(N):
    total_time.append(total_time[i]+waiting_time[i])
    
print(sum(total_time))