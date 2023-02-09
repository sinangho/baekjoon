num = [1]*10001

for i in range(1, 10000):
    dp = i
    i = str(i)
    for j in i:
        dp+=int(j)
    
    if dp > 9993:
        break
    
    num[dp] = 0
    
for i in range(1,10000):
    if num[i] == 1:
        print(i)
    
    