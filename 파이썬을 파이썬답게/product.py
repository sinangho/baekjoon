import itertools

a = "AB"
b = "12"
c = 'ㄱㄴ'

print(list(itertools.product(a,b,c)))