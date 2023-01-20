import sys
input_word_list = []

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    input_word = sys.stdin.readline().rstrip()
    for j in range(0, len(input_word)-1):
        if input_word[j] == input_word[j+1]:
            continue
        elif input_word[j] in input_word[j+1:]:
            N-=1
            break
print(N)