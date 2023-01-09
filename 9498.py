score = int(input())

# if score >= 90:
#     score = 'A'
# elif score >= 80:
#     score = 'B'
# elif score >= 70:
#     score = 'C'
# elif score >= 60:
#     score = 'D'
# else:
#     score = 'F'

# print(score)
temp = ['F','D','C','B','A','A']
for i in range(59, 110, 10):
    if score <= i:
        print(temp[(i//10)-5])
        break