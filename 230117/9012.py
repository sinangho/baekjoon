import sys

N = int(sys.stdin.readline().rstrip())
VPS_Check = 0
VPS = []

for _ in range(N):
    input_str = list(sys.stdin.readline().rstrip())
    
    for i in input_str:
        if i == "(":
            VPS_Check += 1
        elif i == ")":
            VPS_Check -= 1
        
        if VPS_Check == -1:
            break
        
    if VPS_Check == 0:
        VPS.append("YES")

    else:
        VPS.append("NO")
    
    VPS_Check =0 
        
for i in VPS:
    print(i)