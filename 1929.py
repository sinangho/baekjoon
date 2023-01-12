import sys

start, end = map(int, sys.stdin.readline().rstrip().split())
            
num_list = [0]*(end+1)

num_list[0] = num_list[1] = 1

for i in range(2, int(end**0.5)+1, 1):
    if num_list[i] == 0:
        for j in range(i*2, len(num_list), i):
            num_list[j] = 1
            
            
for i in range(start, len(num_list)):
    if num_list[i] == 0:
        print(i)

# f = open('나의 소수.txt', 'w')
# for i in range(start, len(num_list)):
#     if num_list[i] == 0:
#         f.write(str(i)+" ")
# f.close
# print("finish")