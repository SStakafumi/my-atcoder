n = int(input())
a = [list(map(lambda x: int(x) - 1, input().split()))[2:] for _ in range(n)]

d = [0]*n
f = [0]*n
t = 0


def dfs(i):
    global t
    if d[i] == 0:
        t += 1
        d[i] = t
        for j in a[i]:
            dfs(j)
        t += 1
        f[i] = t


while(min(d) == 0):
    dfs(d.index(0))

for i in range(n):
    print(i + 1, d[i], f[i])
