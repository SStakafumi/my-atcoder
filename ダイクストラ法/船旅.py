import sys
import heapq
def input(): return sys.stdin.readline().rstrip()


INF = float('INF')

# 入力
N, K = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(K):
    message = list(map(int, input().split()))
    # 新航路メッセージ
    if message[0] == 1:
        v1, v2, p = message[1:]
        graph[v1].append((v2, p))  # v1-1 → v2-1 料金: p
        graph[v2].append((v1, p))
    # 客からのメッセージ
    else:
        s, g = message[1:]  # スタートとゴール

        h = [(0, s)]  # はじめの距離, 頂点
        visited = [False] * (N+1)

        dp = [INF] * (N+1)  # 各頂点までの距離をINFで初期化
        dp[s] = 0

        while h:
            dist, v1 = heapq.heappop(h)
            if visited[v1]:
                continue
            visited[v1] = True
            targets = graph[v1]
            for target in targets:
                v2, p = target
                if dp[v2] > dp[v1]+p:
                    dp[v2] = dp[v1]+p
                    heapq.heappush(h, (dp[v2], v2))

        if dp[g] == INF:
            print(-1)
        else:
            print(dp[g])
