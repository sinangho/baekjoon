import sys

sub = int(sys.stdin.readline().rstrip())

score = []*sub

score = list(map(int, sys.stdin.readline().rstrip().split()))

max = score[0]
sum = 0

for i in range(1, sub):
    if max < score[i]:
        max = score[i]
        
for i in range(sub):
    score[i] = score[i]/max*100
    sum += score[i]
    
print(sum/sub)
    
