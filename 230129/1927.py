import sys
import heapq

N = int(sys.stdin.readline().rstrip())

num_list = []

for _ in range(N):
    command = int(sys.stdin.readline().rstrip())
    
    if command == 0 and num_list:
        print(heapq.heappop(num_list))
    elif command == 0 and not num_list:
        print(0)
    else:
        heapq.heappush(num_list, command)