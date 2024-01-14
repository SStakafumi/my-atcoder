import sys
def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())

INF = float('inf')
graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    # 頂点iから頂点まではコスト0
    graph[i][i] = 0
for m in range(M):
    a, b, c = map(int, input().split())
    # graph[a][b] = 頂点aからbへコストがcかかる(INFだとコスト無限で行けない)
    graph[a][b] = c
    # graph[b][a] = c # 無向グラフで追加


ans = 0

# 幅が小さい順に見ていく
for k in range(1, N+1):
    # スタート頂点
    for s in range(1, N+1):
        # ゴール頂点
        for t in range(1, N+1):
            graph[s][t] = min(graph[s][t], graph[s][k] + graph[k][t])
            if graph[s][t] < INF:
                ans += graph[s][t]

print(ans)
