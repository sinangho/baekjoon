s, n = input().strip().split(' ')
n = int(n)

print(s)
print(s.rjust((n-len(s))//2)) 
#print(s.center(n))
print(s.rjust(n))