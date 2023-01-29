import collections
import sys

N = int(sys.stdin.readline().rstrip())

Deque = collections.deque()

for _ in range(N):
    command = list(map(str, sys.stdin.readline().rstrip().split()))
    
    cmd = command[0]
    
    if cmd == "push_front":
        Deque.appendleft(command[1])
    elif cmd == "push_back":
        Deque.append(command[1])
    elif cmd == "pop_front":
        if Deque:
            print(Deque.popleft())
        else:
            print(-1)
    elif cmd == "pop_back":
        if Deque:
            print(Deque.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(Deque))
    elif cmd == "empty":
        if Deque:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if Deque:
            print(Deque[0])
        else:
            print(-1)
    elif cmd == "back":
        if Deque:
            print(Deque[len(Deque)-1])
        else:
            print(-1)