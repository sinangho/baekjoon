import sys

answer = []

while True:
    temp=[]
    input_str = sys.stdin.readline().rstrip()
    
    if input_str == ".":
        break
    
    for i in input_str:
        if i == ")" or i == "]":
            if temp:
                a = temp.pop()
                if a == '[' and i == ')':
                    answer.append("no")
                    break
                elif a == '(' and i == ']':
                    answer.append("no")
                    break
            else:
                answer.append("no")
                break
        elif i == '(' or i == '[':
            temp.append(i)
            
    else:
        if temp:
            answer.append("no")
        else:
            answer.append("yes")
for i in answer:
    print(i)