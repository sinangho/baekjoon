N = int(input())
input_word = []

for _ in range(N):
    input_word.append(input())

input_word = list(set(input_word))
input_word.sort(key=lambda x: (len(x), x))

for i in input_word:
    print(i)