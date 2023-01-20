N, K = map(int, input().split())
unit = []
cnt=0
temp = []
for _ in range(N):
    unit.append(int(input()))
    
    
for _ in range(N):
    coin = unit.pop()
    if K//coin>0:
        cnt += K//coin
        K %= coin
# unit.reverse()
# temp.append([K//money if K//money>0 else K%=money for money in unit])


print(cnt)