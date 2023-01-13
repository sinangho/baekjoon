import sys

myword = sys.stdin.readline().rstrip()
word = []

for i in myword:
    word.append(i.upper())

myword = word

alphabet = []
num = [0]*26
check = 0
max_index = 0

for i in range(26):
    alphabet.append(chr(65+i))

for i in myword:
    for j in range(26):
        if i == alphabet[j]:
            print(i, alphabet[j])
            num[j] += 1

max = num[0]    
            
for i in range(26):
    if max < num[i]:
        max = num[i]
        max_index = i

num.sort()

if num[25] == num[24]:
    print("?")
    sys.exit(0)


print(chr(65+max_index))