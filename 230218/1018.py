import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

board = []

line = ['B','W','B','W','B','W','B','W']
line2 = ['W','B','W','B','W','B','W','B']
normal_b = []
normal_b_2 = []

for i in range(4):
    normal_b.append(line)
    normal_b.append(line2)
    normal_b_2.append(line2)
    normal_b_2.append(line)

for i in range(N):
    line = sys.stdin.readline().rstrip()
    temp = []
    for j in line:
        temp.append(j)
    board.append(temp)
    
width = 0
height = 0
change = 65

while (height+7) != N:
    cnt = 0
    cnt2 = 0
    for i in range(height, height+8):
        for j in range(width, width+8):
            if board[i][j] != normal_b[i%8][j%8]:
                cnt +=1
            if board[i][j] != normal_b_2[i%8][j%8]:
                cnt2 += 1
    if cnt > cnt2:
        min = cnt2
    else:
        min = cnt
    if min < change:
        change = min
        
    width+=1
    if width+8 > M:
        width = 0
        height+=1
        
print(change)