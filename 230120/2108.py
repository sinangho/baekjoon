from collections import Counter
import sys

def 최빈값(numlist):
    
    num = Counter(numlist).most_common()
    
    a = num[0][1] 
    b = num[1][1]

    return num[1][0] if a==b else num[0][0]
    
N = int(input())

number = []
for _ in range(N):
    number.append(int(sys.stdin.readline().rstrip()))

number.sort()

if N > 1:
    print(round(sum(number)/N))
    print(number[N//2])
    print(최빈값(number))
    print(max(number) - min(number))
else:
    print((str(number[0])+"\n")*3, end="")
    print(0)