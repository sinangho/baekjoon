H, M = map(int, input().split())

H *= 60

minute = H+M-45

if minute < 0:
    minute += 1440 
    
print(minute//60, minute%60)