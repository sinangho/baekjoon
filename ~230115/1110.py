num = int(input())

temp = num
cnt = 0 

while True:
    a = temp//10
    b = temp%10
    temp = b*10+((a+b)%10)
    cnt+=1
    if temp == num:
        break
    
print(cnt)