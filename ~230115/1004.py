test_cnt = int(input())

planet_info = []
temp = []
cnt_list = []

for i in range(test_cnt):
    x1, y1, x2, y2= map(int, input().split())
    
    planet_cnt = int(input())
    
    cnt = 0
    for j in range(planet_cnt):
        
        a,b,c = list(map(int, input().split()))
        
        distance_sp = ((x1-a)**2 + (y1-b)**2)**0.5
        distance_ep = ((x2-a)**2 + (y2-b)**2)**0.5
        
        if distance_sp < c:
            if distance_ep < c:
                continue
            elif distance_ep > c:
                cnt += 1
        elif distance_sp > c:
            if distance_ep < c:
                cnt += 1
            elif distance_ep > c:
                continue
        
    cnt_list.append(cnt)
        
for i in cnt_list:
    print(i)
