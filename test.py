import sys 

N = int(sys.stdin.readline().rstrip())
RGB = [[0,0,0]]*(N+1)
cost = [0]*3

print(RGB)
print(RGB[0][0])
RGB[1][0] = 2
print(RGB)