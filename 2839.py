import sys

sugar = int(input())

max = sugar // 5

for i in range(max, -1, -1):
    sugar_calc = sugar - 5*i
    if sugar_calc % 3 == 0:
        three = sugar_calc // 3
        print(i+three)
        sys.exit(0)
        
print(-1)