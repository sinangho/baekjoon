answer = []

while True:
    N = list(map(int, input()))
    
    if N[0] == 0:
        break
    
    else:
        R = list(reversed(N))
        
        if N == R:
            answer.append("yes")
        else:
            answer.append("no")
        
for i in answer:
    print(i)