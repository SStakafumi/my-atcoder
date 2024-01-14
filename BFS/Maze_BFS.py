from collections import deque

R, C = map(int, input().split())
sy, sx = map(lambda x: int(x)-1, input().split())
gy, gx = map(lambda x: int(x)-1, input().split())
maze = [list(input()) for _ in range(R)]

dist = [[-1]*C for _ in range(R)]
dist[sy][sx] = 0

d = deque([[sy, sx]])

while d:  # dに一つでも要素が入っているときは処理を続ける
    if dist[gy][gx] != -1:
        break
    v = d.popleft()
    for surPos in [[v[0]-1, v[1]], [v[0], v[1]+1], [v[0]+1, v[1]], [v[0], v[1]-1]]:
        if surPos[0] >= 0 and surPos[1] >= 0:
            if dist[surPos[0]][surPos[1]] != -1 or maze[surPos[0]][surPos[1]] == "#":
                continue
            dist[surPos[0]][surPos[1]] = dist[v[0]][v[1]] + 1
            d.append(surPos)

print(dist[gy][gx])
