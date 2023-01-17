import sys

cmd_cnt = int(sys.stdin.readline().rstrip())
cmd_list = [0.1]*(cmd_cnt*2)
stack = []

for i in range(cmd_cnt):
    temp = []
    temp.append(sys.stdin.readline().rstrip().split())
    temp[0].append("")
    
    if temp[0][1] == "":
        cmd_list[i*2] = temp[0][0]
    else:
        cmd_list[i*2] = temp[0][0]
        cmd_list[i*2+1] = int(temp[0][1])

for i in range(cmd_cnt):
    if cmd_list[i*2] == 'push':
        stack.append(cmd_list[i*2+1])
        
    elif cmd_list[i*2] == 'pop':
        if stack:
            temp = stack.pop()
            print(temp)
        else:
            print(-1)
            
    elif cmd_list[i*2] == 'size':
        print(len(stack))
        
    elif cmd_list[i*2] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif cmd_list[i*2] == 'top':
        if stack:
            temp = stack.pop()
            print(temp)
            stack.append(temp)
        else:
            print(-1)          