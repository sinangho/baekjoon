s = list(map(str, input()))
cnt = 0
for i in range(1, len(s)): 
    if s[i-1] != s[i]:
       cnt += 1 

if cnt == 1:
    print(1)
elif cnt % 2 != 0:
    print(cnt//2+1)
else:
    print(cnt//2)
