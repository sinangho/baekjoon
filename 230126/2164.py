import collections
import sys

N = int(sys.stdin.readline().rstrip())

card = [i for i in range(N, 0, -1)]
card = collections.deque(card)

for _ in range(N-1):
    card.pop()
    card.insert(0, card.pop())
    
print(card[0])
    
