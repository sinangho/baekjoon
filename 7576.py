import sys
M, N = map(int, input().split())
date = 0
temp = []
box = []
ripen_tomato = []
ripe = 1
break_token = 0
cant_ripe = 0

for i in range(M+2):
    temp.append(3)
    
box.append(temp)

for i in range(N):
    temp=[]
    temp = list(map(int, input().split()))
    temp.insert(0, 3)
    temp.append(3)
    box.append(temp)

temp = []
for i in range(M+2):
    temp.append(3)

box.append(temp)

def show_tomato():
    for i in range(N):
        for j in range(M):
         print(box[i+1][j+1],end="")
        print("")

def check_tomato():
    global break_token
    sum = 0
    no_tomato = 0
    for i in range(N):
        for j in range(M):
            if box[i+1][j+1] == 0 or box[i+1][j+1] == -1:
                sum+=1
            if box[i+1][j+1] == -1:
                no_tomato += 1
    
    if  no_tomato == N*M or sum == N*M:
        print(-1)
        sys.exit(0)
    
    for i in range(N):
        for j in range(M):
            if box[i+1][j+1] == 1:
                ripe = 1
            elif box[i+1][j+1] == 0:
                ripe = 0
                break_token = 1
                break
        if break_token == 1:
            break_token = 0
            break
        
    if ripe == 1:
        # print(date,"강종, 다 익었다")
        print(date)
        sys.exit(0)

check_tomato()

while True:
    for i in range(N):
        for j in range(M):
            if box[i+1][j+1] == 1:
                # print("익은 토마토 발견",i+1,j+1)
                ripen_tomato.append(i+1)
                ripen_tomato.append(j+1)
                box[i+1][j+1] = 2
                cant_ripe = 0

    # for i in range(len(ripen_tomato)//2):
    #     a = ripen_tomato[i*2]
    #     b = ripen_tomato[i*2+1]
    #     if box[a][b+1] == 0:
    #         box[a][b+1] = 1
    #         cant_ripe = 0
    #     elif box[a][b+1] == 2 or box[a][b+1] == -1 or box[a][b+1] == 3:
    #         cant_ripe += 1
    #     if box[a][b-1] == 0:
    #         box[a][b-1] = 1
    #         cant_ripe = 0
    #     elif box[a][b-1] == 2 or box[a][b-1] == -1 or box[a][b-1] == 3:
    #         cant_ripe += 1
    #     if box[a+1][b] == 0:
    #         box[a+1][b] = 1
    #         cant_ripe = 0
    #     elif box[a+1][b] == 2 or box[a+1][b] == -1 or box[a+1][b] == 3:
    #         cant_ripe += 1
    #     if box[a-1][b] == 0:
    #         box[a-1][b] = 1
    #         cant_ripe = 0
    #     elif box[a-1][b] == 2 or box[a-1][b] == -1 or box[a-1][b] == 3:
    #         cant_ripe += 1
        
    #     if cant_ripe == (len(ripen_tomato)//2)*4:
    #         print(-1)
    #         sys.exit(0)
    
    for i in range(len(ripen_tomato)//2):
        a = ripen_tomato[i*2]
        b = ripen_tomato[i*2+1]
        if box[a][b+1] == 0:
            box[a][b+1] = 1
            cant_ripe = 0
        else:
            cant_ripe += 1
        if box[a][b-1] == 0:
            box[a][b-1] = 1
            cant_ripe = 0
        else:
            cant_ripe += 1
        if box[a+1][b] == 0:
            box[a+1][b] = 1
            cant_ripe = 0
        else:
            cant_ripe += 1
        if box[a-1][b] == 0:
            box[a-1][b] = 1
            cant_ripe = 0
        else:
            cant_ripe += 1
        
        if cant_ripe == (len(ripen_tomato)//2)*4:
            print(-1)
            sys.exit(0)
            
    date += 1
    ripen_tomato = []
    # print("하루가 지나갑니다..")
    check_tomato()
    # show_tomato()
                    
