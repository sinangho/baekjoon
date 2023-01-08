1002
import math

num = int(input())
answer = []

for i in range(0, num, 1):
    
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    distance = ((x1-x2)**2 + (y1-y2)**2) **0.5
    
    if x1==x2 and y1==y2 and r1==r2:
        answer.append(-1)
    else:
        if (r1+r2) > distance and abs(r1-r2) < distance:
            answer.append(2)
        elif (r1+r2) == distance or abs(r1-r2) == distance:
            answer.append(1)
        elif (r1+r2) < distance or abs(r1-r2) > distance:
            answer.append(0)
        
    
for i in range(num):
    print(answer[i])