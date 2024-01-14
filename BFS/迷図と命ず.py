from collections import deque

while True:
    w, h = map(lambda x: 2*int(x)-1, input().split())  # 予め壁込みのw,hを考える
    if w == -1 and h == -1:
        break
    graph = [[0]*(w) for _ in range(h)]
    for i in range(h):
        row = list(map(int, input().split()))
        if i & 1:
            for j, r in enumerate(row):
                graph[i][2*j] = r
        else:
            for j, r in enumerate(row):
                graph[i][2*j+1] = r

    d = deque([[0, 0]])
    dist = [[-1]*(w) for _ in range(h)]
    dist[0][0] = 1

    # BFS
    while d:
        if dist[h-1][w-1] != -1:
            break
        v = d.popleft()
        vr, vc = v[0], v[1]
        for sp in [[vr-2, vc, vr-1, vc], [vr, vc+2, vr, vc+1], [vr+2, vc, vr+1, vc], [vr, vc-2, vr, vc-1]]:
            if 0 <= sp[0] < h and 0 <= sp[1] < w:
                if dist[sp[0]][sp[1]] != -1 or graph[sp[2]][sp[3]] == 1:
                    continue
                d.append(sp)
                dist[sp[0]][sp[1]] = dist[vr][vc] + 1

    if dist[h-1][w-1] == -1:
        print(0)
    else:
        print(dist[h-1][w-1])
