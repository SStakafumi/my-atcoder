import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
point = [0] * (N+1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for _ in range(Q):
    p, x = map(int, input().split())
    point[p] += x
# dfsを用いて累積和を計算する
# 初期状態だと前の値がないためデフォルト引数に-1を代入


def dfs(now, prev):
    for next in graph[now]:
        # 次のノードが前に参照した値の時はcontinue
        if next == prev:
            continue
        # 現在の値を次のポイントに加算することで累積和をとる
        point[next] += point[now]
        # 次のノードと現在のノードを引数にdfsを継続する
        dfs(next, now)


dfs(1, 0)
print(*point[1:])

""" 
# 自分の回答 (WA)
N, Q = map(int, input().split())

tree = [[] for _ in range(N+1)]

# 木作成
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 念の為ソート
for i in range(N+1):
    tree[i].sort()

ans = [0]*(N+1)
throghNum = []


def DFS(now, prev):
    throghNum.append(now)
    for next in tree[now]:
        if next != prev:
            DFS(next, now)


PX = [list(map(int, input().split())) for _ in range(Q)]

for p, x in PX:
    DFS(p, p-1)
    for n in throghNum:
        ans[n] += x
    throghNum = []

print(ans[1:])
"""
