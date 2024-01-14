from collections import deque

h, w = map(int, input().split())

graph = []
iniWall = 0
for i in range(h):
    graph.append(list(input()))
    iniWall += graph[i].count("#")

dist = [[-1]*w for _ in range(h)]
dist[0][0] = 1

d = deque([[0, 0]])

while d:
    if dist[h-1][w-1] != -1:
        break
    v = d.popleft()
    vr, vc = v
    for sp in [[vr-1, vc], [vr, vc+1], [vr+1, vc], [vr, vc-1]]:
        if 0 <= sp[0] < h and 0 <= sp[1] < w:
            if dist[sp[0]][sp[1]] != -1 or graph[sp[0]][sp[1]] == "#":
                continue
            d.append(sp)
            dist[sp[0]][sp[1]] = dist[v[0]][v[1]] + 1

print(-1 if dist[h-1][w-1] == -1 else h*w-iniWall-dist[h-1][w-1])
