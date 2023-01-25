N, K = map(int, input().split())

circle = [i for i in range(1, N+1)]
temp = []
index = 0

for i in range(N):
    index += K-1
    if index >= len(circle):
        index %= len(circle)
    temp.append(str(circle[index]))
    circle.pop(index)

print("<",', '.join(temp),">", sep="")