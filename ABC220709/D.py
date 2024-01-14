import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
X = []
Y = []
R = []

sx, sy, tx, ty = map(int, input().split())

S = [sx, sy]
T = [tx, ty]

sgroup = []
tgroup = []

for _ in range(N):
    x, y, r = map(int, input().split())
    X.append(x)
    Y.append(y)
    R.append(r)


def distance(p1, p2):
    dist = (p1[0]-p2[0])**2 + (p2[1]-p2[1])**2
    return dist


graph = [[] for _ in range(N+1)]

for i in range(N):
    l = []
    for j in range(N):
        if distance([X[i], Y[i]], [X[j], Y[j]]) <= (R[i]+R[j])**2:
            l.append(j+1)
    graph[i+1] = l
    graph[i+1].sort()


findTime = [0]*(N+1)  # 発見時間リスト
finishedTime = [0]*(N+1)  # 完了時間リスト
visited = [False] * (N+1)  # 訪問したかリスト
visitSequence = []  # 訪問順リスト


# DFS
def dfs(now, prev, time):
    if visited[now]:
        # すでに訪問済みならその時の時間を返す
        return time
    # 訪れていないので訪れたことにする
    visited[now] = True
    visitSequence.append(now)

    # 初めて訪れた時間を記録
    findTime[now] = time

    for nxt in graph[now]:
        if visited[nxt]:
            # 次の場所がすでに訪問済みならおとづれない
            continue
        time = dfs(nxt, now, time+1)
        visitSequence.append(now)

    # このfor文が終了したらnowより深い部分はすべて調査し終わった
    # 戻るときに時間をすすめる
    time += 1
    # 完了時間を記録
    finishedTime[now] = time

    return time


for i in range(N):
    if distance(S, [X[i], Y[i]]) == R[i]**2:
        sgroup.append(i)
    if distance(T, [X[i], Y[i]]) == R[i]**2:
        tgroup.append(i)


# 孤立ノードを考慮し、DFSを開始
gtime = 0
for i in sgroup:
    if not visited[i]:
        gtime += 1
        gtime = dfs(i, i-1, gtime)

for id, d, f in zip(range(1, N+1), findTime[1:], finishedTime[1:]):
    print(id, d, f)
