import heapq

#--------------------------------------[入力受取]--------------------------------------#
INF = float('INF')
V, E, sv = map(int, input().split())  # 頂点数, 辺数, スタート頂点
graph = [[] for _ in range(V)]
for _ in range(E):
    v1, v2, c = map(int, input().split())  # 辺v1→v2 c:重み
    graph[v1].append((v2, c))
    # graph[v2].append(v1, c) # 無効グラフでは追加

#--------------------------------------[初期値]--------------------------------------#
dp = [INF] * V  # 各頂点までの距離をINFに設定
visited = [False] * V  # 訪問済みか
dp[sv] = 0  # 始点の距離 = 0
h = [(0, sv)]  # [(距離,頂点)] はじめ距離0で初期頂点svにいる

#--------------------------------------[探索開始]--------------------------------------#
while h:
    c, v1 = heapq.heappop(h)  # 距離が小さい順に取り出す
    # すでに訪問済みだとなにもしない
    if visited[v1]:
        continue
    # 訪れたことにする
    visited[v1] = True
    # 行ける(頂点, 重み)を格納
    targets = graph[v1]
    for target in targets:
        v2, c = target  # 次の頂点, 重み
        # より短い経路があるのであれば更新
        if dp[v2] > dp[v1] + c:
            dp[v2] = dp[v1] + c
            heapq.heappush(h, (dp[v2], v2))  # 新しく距離と頂点を追加


#--------------------------------------[回答]--------------------------------------#
for answer in dp:
    if answer == INF:
        print('INF')
    else:
        print(answer)
