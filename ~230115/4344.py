num = int(input())
temp = []
score = []
avg_rate = []


for i in range(num):
    temp = list(map(int, input().split()))
    score.append(temp)
    
for i in range(num):
    sum=0
    cnt=0
    for j in range(1,len(score[i])):
        sum += score[i][j]
    avg = sum / score[i][0]
    
    for j in range(1,len(score[i])):
        if score[i][j] > avg:
            cnt += 1
    rate = cnt/score[i][0]
    rate = format(rate*100, '.3f')
    avg_rate.append(rate)
    
for i in avg_rate:
    print(i+"%")