import sys
import heapq
from collections import deque

# 入力処理高速化


def input(): return sys.stdin.readline().rstrip()


N, K = map(int, input().split())
C = [0]
R = [0]
for _ in range(N):
    c, r = map(int, input().split())
    C.append(c)
    R.append(r)

INF = float('INF')
# オリジナルのグラフ

graph = [[] for _ in range(N+1)]
for _ in range(K):
    a, b = map(int, input().split())
    # 料金がINFとしてPathを通す
    graph[a].append(b)
    graph[b].append(a)

# BFSをもとに重みをつけたグラフ
newGraph = [[] for _ in range(N+1)]
# BFS
for i in range(1, N+1):
    d = deque([i])
    dist = [-1] * (N+1)
    dist[i] = 0

    while d:
        v = d.popleft()
        for gv in graph[v]:
            # もし訪問していたら何もしない
            if dist[gv] != -1:
                continue
            # もしタクシーで行ける範囲であればBFS
            if dist[v] < R[i]:
                dist[gv] = dist[v]+1
                d.append(gv)
    # 町iから行ける町へタクシー料金の重み付けをする
    for j, d in enumerate(dist[1:]):
        if d != -1 and d != 0:
            newGraph[i].append((C[i], j+1))  # 料金, 頂点(町)


# ダイクストラ法
h = [(0, 1)]
visited = [False] * (N+1)
fare = [INF] * (N+1)
fare[1] = 0

while h:
    _, v1 = heapq.heappop(h)
    if visited[v1]:
        continue
    visited[v1] = True
    for f, v2 in newGraph[v1]:
        if fare[v2] > fare[v1] + f:
            fare[v2] = fare[v1] + f
            heapq.heappush(h, (fare[v2], v2))

print(fare[N])
