import collections

my_str = list(input().strip())
my_str.sort()
my_str = collections.Counter(my_str)
