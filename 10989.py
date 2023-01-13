import sys

numberList = [0]*10001

num = int(sys.stdin.readline().rstrip())

for i in range(1, num+1):
    num = int(sys.stdin.readline().rstrip())
    numberList[num] += 1

for i in range(1, len(numberList)):
    if numberList[i] != 0:
        for j in range(numberList[i]):
            print(i)
    