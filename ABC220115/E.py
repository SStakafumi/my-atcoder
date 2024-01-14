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


N, M, Q = map(int, input().split())
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((-1, a-1, b-1, c))

for i in range(Q):
    u, v, w = map(int, input().split())
    edges.append((i, u-1, v-1, w))

# クラスカル
edges.sort(key=lambda t: t[3])
ans = [False] * Q
uf = UnionFind(N)

for i, s, t, w in edges:
    if i == -1:
        uf.unite(s, t)
    else:
        if not uf.same(s, t):
            ans[i] = True

for i in range(Q):
    if ans[i]:
        print("Yes")
    else:
        print("No")
