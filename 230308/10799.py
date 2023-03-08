
ls = list(input())
temp = []
cnt = 0

for i in range(len(ls)):
    if ls[i] == "(":
        temp.append("(")
    else:
        if ls[i-1] == "(":
            temp.pop()
            cnt += len(temp)
        else:
            temp.pop()
            cnt+=1
            
print(cnt)