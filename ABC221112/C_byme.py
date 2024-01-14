from collections import deque

N = int(input())
graph = dict()
visited = dict()

for _ in range(N):
    a, b = map(int, input().split())
    visited[a] = False
    visited[b] = False
    if a not in graph:
        graph[a] = []
    graph[a].append(b)
    if b not in graph:
        graph[b] = []
    graph[b].append(a)
    
que = deque([1])

while que:
    now = que.popleft()
    if now not in graph:
        continue
    if visited[now]:
        continue
    visited[now] = True
    
    for nex in graph[now]:
        if visited[nex]:
            continue
        que.append(nex)

ans = 1

for k, v in visited.items():
    if v:
        ans = max(ans, k)

print(ans)
        