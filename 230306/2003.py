N, M = map(int, input().split())

A = list(map(int, input().split()))

cnt, start, end = 0, 0, 1

while end <= N:
    temp = A[start:end]
    A_sum = sum(temp)
    
    if A_sum < M:
        end+=1
    elif A_sum > M:
        start+=1
    else:
        cnt+=1
        end+=1

print(cnt)