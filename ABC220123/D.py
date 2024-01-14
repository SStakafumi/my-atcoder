import itertools
N = int(input())

l = list(range(1, N+1))
print(l)
for i in list(itertools.combinations(l, 2)):
    print(i)
