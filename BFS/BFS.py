from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 与えられるグラフが有向グラフのときはこれを外せる

dist = [-1] * (n+1)
# dist[0] = 0
dist[1] = 0

d = deque([1])

while d:  # dに一つでも要素が入っているときは処理を続ける
    v = d.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v]+1
        d.append(i)

print(*dist[1:], sep="\n")
