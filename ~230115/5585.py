import sys

money = int(sys.stdin.readline().rstrip())
coin = 0
money = 1000-money
standard = 500

for i in range(6):
    if money//standard > 0:
        coin+= money//standard
        money %= standard
    if i % 2 == 0:
        standard //= 5
    else:
        standard //= 2

print(coin)