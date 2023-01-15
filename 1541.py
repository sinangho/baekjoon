import sys

fomula = sys.stdin.readline().rstrip().split("-")

sum_list = []

for i in fomula:
    sum_list.append(sum(map(int, i.split('+'))))
    
print(sum_list)
    
print(sum_list[0] - sum(sum_list[1:]))