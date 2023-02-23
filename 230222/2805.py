import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
tree = list(map(int, sys.stdin.readline().rstrip().split()))

start, end = 0, max(tree)

while start <= end:
    
    mid = (start+end)//2
    take_sum = 0
    
    for i in tree:
        if i > mid:
            take_sum += i - mid
    
    if take_sum < M:
        end = mid-1
    else:
        answer = mid
        start = mid+1
        
print(answer)