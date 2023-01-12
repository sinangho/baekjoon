import sys
temp = []
index = 0
che = 2
a, b = map(int, sys.stdin.readline().rstrip().split())

num = []

for i in range(2, b):
    num.append(i)

while True:
    while True:
        if num[i] % che == 0:
            num.pop(i)
            if i < len(num):
                i += 1
    che += 1
    if che == b:
        break
            


for i in temp:
    print(i)