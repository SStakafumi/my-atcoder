from collections import deque

h, w, n = map(int, input().split())
maiz = [list(input()) for _ in range(h)]

# 巣及び工場の位置をリストposに格納
pos = []
for i in range(n+1):
    for col, row in enumerate(maiz):
        try:
            if i == 0:
                pos.append([col, row.index("S")])
                break
            else:
                pos.append([col, row.index(str(i))])
                break
        except ValueError:
            pass

totalDist = 0

for i in range(n):
    s = pos[i]
    g = pos[i+1]

    dist = [[-1]*w for _ in range(h)]
    dist[s[0]][s[1]] = 0

    d = deque([s])

    while d:
        if dist[g[0]][g[1]] != -1:
            break
        v = d.popleft()
        for sp in [[v[0]-1, v[1]], [v[0], v[1]+1], [v[0]+1, v[1]], [v[0], v[1]-1]]:
            if 0 <= sp[0] < h and 0 <= sp[1] < w:
                if dist[sp[0]][sp[1]] != -1 or maiz[sp[0]][sp[1]] == "X":
                    continue
                dist[sp[0]][sp[1]] = dist[v[0]][v[1]] + 1
                d.append(sp)

    totalDist += dist[g[0]][g[1]]


print(totalDist)
