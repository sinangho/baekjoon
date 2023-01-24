import sys

month = []
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month.append(0)
for i in range(1, 13):
    if i == 4 or i == 6 or i == 9 or i == 11:
        month.append(30)
    elif i == 2:
        month.append(28)
    else:
        month.append(31)

date = 0
m, d = map(int, sys.stdin.readline().rstrip().split())

date += d

for i in range(m):
    date += month[i]
    
print(day[date%7])
