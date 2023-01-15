import sys

num = int(sys.stdin.readline().rstrip())
conference_schedule = []
temp = []
pop_index = []
del_cnt = 0

for i in range(num):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    conference_schedule.append(temp)
    
conference_schedule.sort()
    
for i in range(num):
    for j in range(i+1, num):
        if conference_schedule[i][0] == conference_schedule[j][0]:
            if conference_schedule[i][1] >= conference_schedule[j][1]:
                conference_schedule[i][0] = 30
            elif conference_schedule[i][1] < conference_schedule[j][1]:
                conference_schedule[j][0] = 30

conference_schedule.sort()

for i in range(num):
    if conference_schedule[i][0] == 30:
        del_cnt = num - i
        break

for i in range(del_cnt):
    conference_schedule.pop()

case_1 = []
case_2 = []
case_1_start_index = 0
case_2_start_index = 1
      
for k in range(len(conference_schedule)//2+1):
    
    case_1_index = 0
    case_2_index = 0
    case_2 = []
    case_1 = []

    case_1.append(conference_schedule[case_1_start_index])
        
    for i in range(case_1_index, len(conference_schedule)):
        if case_1[case_1_index][1] <= conference_schedule[i][0]:
            case_1.append(conference_schedule[i])
            case_1_index += 1
            
    case_2.append(conference_schedule[case_2_start_index])

    for i in range(case_2_index+1, len(conference_schedule)):
        if case_2[case_2_index][1] <= conference_schedule[i][0]:
            case_2.append(conference_schedule[i])
            case_2_index += 1
    
    if len(case_1) > len(case_2):
        if case_1_start_index < case_2_start_index:
            case_2_start_index += 1
        else:
            case_2_start_index = case_1_start_index+1
        
    elif len(case_2) > len(case_1):
        if case_1_start_index > case_2_start_index:
            case_1_start_index += 1
        else:
            case_1_start_index = case_2_start_index+1

if len(case_1) > len(case_2):
    print(len(case_1))
else:
    print(len(case_2))