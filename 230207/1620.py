import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

pokemon_list = {}
pokemon_list2 = {}
output = []

for i in range(1, N+1):
    temp = sys.stdin.readline().rstrip()
    pokemon_list[temp] = i
    pokemon_list2[i] = temp
    
for i in range(M):
    
    command = sys.stdin.readline().rstrip()
    temp = command.isdigit()
    
    if command.isdigit() == True:
        output.append(pokemon_list2.get(int(command)))
    else:
        output.append(pokemon_list.get(command))

for i in output:
    print(i)
    