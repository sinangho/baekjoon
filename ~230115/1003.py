#1003

# 시간 초과
# zero = 0
# one = 0

# def fibo(n):
    
#     global zero
#     global one
        
#     if n == 0:
#         zero += 1
#         return 0
#     elif n == 1:
#         one += 1
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)   
    
# cnt = int(input())
# temp = []

# for i in range(cnt):
#     num = int(input())
#     zero = 0
#     one = 0z
#     fibo(num)
#     temp.append(zero)
#     temp.append(one)
    
# for i in range(cnt):
#     print(temp[i*2], temp[i*2+1])

def fibo(n):
    
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    else:
        a, b =1, 1
        temp = b
        while n != 1:
            temp = b
            b = a
            a += temp
            n = n-1
        
    return temp, b

cnt = int(input())
answer = []

for i in range(cnt):
    num = int(input())
    b, a = fibo(num)
    answer.append(b)
    answer.append(a)

for i in range(cnt):
    print(answer[i*2], answer[i*2+1])