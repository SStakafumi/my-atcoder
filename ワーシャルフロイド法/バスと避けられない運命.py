import sys
def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
INF = float('inf')

graph = [[INF]*N for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a-1][b-1] = t
    graph[b-1][a-1] = t

# ワーシャルフロイド法
for k in range(N):
    for s in range(N):
        for t in range(N):
            graph[s][t] = min(graph[s][k]+graph[k][t], graph[s][t])

maxCost = []

for i in range(N):
    maxCost.append(max(graph[i]))

# print(maxCost.index(min(maxCost))+1) バス停の番号
print(min(maxCost))
