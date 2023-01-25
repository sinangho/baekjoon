import sys

while True:
    try:
        temp = list(map(int, input().split()))
        if not temp:
            break
        print(sum(temp))
    except:
        break