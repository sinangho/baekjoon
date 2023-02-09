height = []

for _ in range(9):
    height.append(int(input()))

break_cnt = 0
sum = sum(height)

for i in range(0, 8):
    for j in range(i+1, 9):
        first = height[i]
        second = height[j]
        temp = sum - first - second
        if temp == 100:
            height.remove(first)
            height.remove(second)
            break_cnt = 1
            break
    if break_cnt == 1:
        break
            
height.sort()

for i in height:
    print(i)