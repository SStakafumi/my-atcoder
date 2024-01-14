### 解法1 ###
""" 
from itertools import permutations


def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)


N = int(input())
l = list(range(N))

perm = list(permutations(l, N))
perml = len(perm)

a = [0]*N
b = [0]*N
for i in range(N):
    a[i], b[i] = map(int, input().split())
ans = 0

for p in perm:
    for i in range(N-1):
        ans += distance(a[p[i]], b[p[i]], a[p[i+1]], b[p[i+1]])

print(ans/perml)
 """

### 解法2 ###
from itertools import combinations

N = int(input())
cities = [list(map(int, input().split())) for _ in range(N)]


def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**(1/2)


sumDis = 0
comb = combinations(cities, 2)

for p1, p2 in comb:
    sumDis += distance(p1[0], p1[1], p2[0], p2[1])

print(2*sumDis/N)
