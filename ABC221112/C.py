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
    # 今いる階にはしごがなければ何もしない
    if now not in visited:
        continue
    # 今いる階に訪れたことがあれば何もしない
    if visited[now]:
        continue
    # 訪れたので履歴を残す
    visited[now] = True
    
    # 今いる階から行ける階について確認
    for nex in graph[now]:
        # もし訪れていれば何もしない
        if visited[nex]:
            continue
        que.append(nex)

ans = 1

for node, vis in visited.items():
    # print(node, vis)
    if vis:
        ans = max(ans, node)

print(ans)
    