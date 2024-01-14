from collections import defaultdict

N = int(input())
d = defaultdict(int)

for i in range(N):
    si = input()
    d[si] += 1
    if d[si] == 1:
        print(si)
    else:
        print(si+'({})'.format(d[si]-1))