N = list(map(int, input()))

if 0 not in N:
    print(-1)
    
else:
    N.remove(0)
    temp = sum(N)
    if temp%3 != 0:
        print(-1)
    else:
        N.sort(reverse=True)
        N.append(0)
        for i in N:
            print(i, end="")