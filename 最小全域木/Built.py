from collections import defaultdict
import sys
def input(): return sys.stdin.readline().rstrip()


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


N = int(input())
city = []
for i in range(N):
    city.append([i] + list(map(int, input().split())))

xCity = sorted(city, key=lambda c: c[1])
yCity = sorted(city, key=lambda c: c[2])

edges = []
for i in range(N-1):
    i1, x1, y1 = xCity[i]
    i2, x2, y2 = xCity[i+1]
    cost = min(abs(x1-x2), abs(y1-y2))
    edges.append((i1, i2, cost))

for i in range(N-1):
    i1, x1, y1 = yCity[i]
    i2, x2, y2 = yCity[i+1]
    cost = min(abs(x1-x2), abs(y1-y2))
    edges.append((i1, i2, cost))

edges.sort(key=lambda c: c[2])
ans = 0
edgeNum = 0
uf = UnionFind(N)
for s, t, w in edges:
    if edgeNum == N-1:
        break
    if uf.same(s, t):
        continue
    uf.unite(s, t)
    ans += w
    edgeNum += 1

print(ans)
