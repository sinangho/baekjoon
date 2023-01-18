import sys

input_str = list(sys.stdin.readline().rstrip())
cnt = 0

while input_str:
    alphabet = input_str.pop()
    
    if alphabet == "=" or alphabet ==  "-" or alphabet == "j":
        if input_str:
            next_alphabet = input_str.pop()
        else:
            cnt+=1
            break
        if next_alphabet == "c" or next_alphabet == "l" or next_alphabet == "n" or next_alphabet == "s" or next_alphabet == "d":
            cnt+=1
        elif next_alphabet == "z":
            if input_str:
                next_alphabet = input_str.pop()
                if next_alphabet == "d":
                    cnt+=1
                else:
                    input_str.append(next_alphabet)
                    cnt+=1
            else:
                cnt+=1
                break
        else:
            input_str.append(next_alphabet)
            cnt+=1
    else:
        cnt+=1
print(cnt) 

# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()

# for i in croatia :
#     word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
# print(len(word))