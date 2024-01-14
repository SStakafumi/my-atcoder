# メモ化再帰で有向非閉路グラフの最長パス長さを求める
# トポロジカルオーダーのほうが早い ('トポロジカルソート.py' 参照)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def chmax(a, b):
    """ 最大値を返す関数(関数作ったほうが早いっぽい) """
    if a >= b:
        return a
    else:
        return b


# 入力
N, M = map(int, input().split())
# 隣接関係は隣接リストで管理する
graph = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    # 最初のindexをゼロにする
    graph[x-1].append(y-1)
# dp[v] := ノードvを始点とした時の有向パスの長さの最大値
# -1 未訪問で初期化。
dp = [-1] * N
# メモ化再帰


def rec(v):
    # 既に更新済み
    if dp[v] != -1:
        return dp[v]
    ans = 0
    lst_nv = graph[v]
    for nv in lst_nv:
        ans = chmax(ans, rec(nv) + 1)
    dp[v] = ans
    return dp[v]


# 全ての点に対して更新する
ans = 0
for v in range(N):
    ans = chmax(ans, rec(v))

print(ans)
