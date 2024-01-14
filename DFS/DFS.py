# 設定
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

# 有向グラフver

'''
Input例
    4       頂点数
    1 1 2   頂点, 接続辺数, 接続頂点
    2 1 4 
    3 0
    4 1 3
'''

N = int(input())  # 頂点数
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    u, k, *v = map(int, input().split())  # 頂点(1,2,...,N), 接続辺数, 接続頂点のリスト
    graph[u] = v
    graph[u].sort()

# # 無効グラフver

# '''
# Input例
#     4 4     頂点数, 接続辺数
#     1 2     つながってる頂点の組
#     2 3
#     2 4
#     3 4
# '''

# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# for i in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)


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


# 孤立ノードを考慮し、全ての頂点からDFSを開始
gtime = 0
for i in range(1, N+1):
    if not visited[i]:
        gtime += 1
        gtime = dfs(i, i-1, gtime)

# Output

# 頂点, 発見時間, 完了時間 を表示
for id, d, f in zip(range(1, N+1), findTime[1:], finishedTime[1:]):
    print(id, d, f)

# 訪問順を一行に表示
print(" ".join(map(str, visitSequence)))

# # 訪問順を一列に表示
# print("\n".join(map(str, visitSequence)))
