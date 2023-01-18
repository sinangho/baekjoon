num = int(input())

for _ in range(4):
    a = int(input())
    num *= a
    if (num**0.5)%2 == 0:
        print("found")
        break
else:
    print("not found")
    
    
