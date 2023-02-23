import sys
N = int(sys.stdin.readline().rstrip())
city = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())

total_reaquire = sum(city)

if M > total_reaquire:
    print(max(city))
    sys.exit(0)
    
start, end = 0, max(city)

while start <= end:
    
    mid = (start+end)//2
    money = 0
    
    for i in city:
        if i > mid:
            money += i - mid
    
    if money < total_reaquire - M:
        end = mid-1
    else:
        answer = mid
        start = mid+1

print(answer)