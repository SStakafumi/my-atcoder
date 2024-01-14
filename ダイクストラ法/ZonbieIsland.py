import sys
import heapq
from collections import deque
# 入力処理高速化
def input(): return sys.stdin.readline().rstrip()


# 入力受付
N, M, K, S = map(int, input().split())
P, Q = map(int, input().split())
C = [int(input()) for _ in range(K)]

# グラフ作成
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# ゾンビがいる島はTrue
zonbieIsland = [False]*(N+1)
for c in C:
    zonbieIsland[c] = True

# 宿泊料を決める
# はじめは危険じゃない島人して考えてP円とする
accomFee = [P]*(N+1)
# ゾンビがいる島の数だけループ
for c in C:
    # 距離とキューの初期化
    dist = [-1] * (N+1)
    dist[c] = 0
    d = deque([c])

    # 幅優先探査(BFS)で危険な島を見つける
    while d:  # dに一つでも要素が入っているときは処理を続ける
        v = d.popleft()
        for i in graph[v]:
            if dist[i] != -1:
                continue
            if dist[v] + 1 <= S:
                dist[i] = dist[v]+1
                d.append(i)

    for i in range(1, N+1):
        # 危険な島だったら料金をQ円に更新
        if dist[i] != -1:
            accomFee[i] = Q

# N番目の島は宿泊料を考えないため0円
accomFee[N] = 0

# ダイクストラ法
INF = float('INF')

fee = [INF]*(N+1)
fee[1] = 0
visited = [False]*(N+1)
h = [(0, 1)]

while h:
    f, v1 = heapq.heappop(h)  # その町までの料金, 頂点 (最小料金のものから優先的に選ぶ)
    if visited[v1]:
        continue
    visited[v1] = True
    # 町v1からつながるすべての町へのコストを確認
    for v2 in graph[v1]:
        # ゾンビ島だったら訪れない
        if not zonbieIsland[v2]:
            # 料金の更新
            if fee[v2] > fee[v1] + accomFee[v2]:
                fee[v2] = fee[v1] + accomFee[v2]
                heapq.heappush(h, (fee[v2], v2))

print(fee[N])
