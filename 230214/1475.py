N = input()

num = [0]*9
cnt = 0
for i in N:
    if i != '9':
        num[int(i)] += 1
    elif i == '9':
        num[6] += 1
        
if num[6]%2 != 0:
    num[6] = num[6]//2 + 1
else:
    num[6] //= 2

print(max(num))

# 