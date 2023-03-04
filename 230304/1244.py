N = int(input())
switch = [2] + list(map(int, input().split()))
M = int(input())
student = []
for i in range(M):
    student.append(list(map(int, input().split())))
    
def change_switch(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    
for i in range(M):
    cnt = 1
    gender = student[i][0]
    pivot = student[i][1]
    if gender == 1:
        for j in range(pivot, N+1, pivot):
            change_switch(j)
            
    elif gender == 2:
        for j in range(N//2):
            if pivot + j > N or pivot - j < 1:
                break
            if switch[pivot+j] == switch[pivot-j]:
                change_switch(pivot+j)
                change_switch(pivot-j)
            else:
                break
        change_switch(pivot)
                    
                
    
for i in range(1, N+1):
    print(switch[i], end=" ")
    if i%20 == 0:
        print()
    
        