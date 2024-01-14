# 有向非閉路グラフ(DAG)に対し、トポロジカルソートをし、最長経路長さ及びトポロジカルオーダーを求める
# ① 入次数(in degree)が入ってない頂点を見つける
# ② ①の頂点以外から作られる誘導グラフを作成する
# ③ ①と②を繰り返す

import sys
from collections import deque


def input():
    # input処理を高速化する
    return sys.stdin.readline().rstrip()


def chmax(a, b):
    """ 最大値を返す関数 """
    if a >= b:
        return a
    return b


def main():
    # 入力
    N, M = map(int, input().split())
    # 隣接関係は隣接リストで管理する
    graph = [[] for _ in range(N)]
    # 各頂点の入力辺の本数(入次数)
    inDeg = [0] * N
    for _ in range(M):
        x, y = map(int, input().split())
        # 最初のindexをゼロにする
        graph[x-1].append(y-1)
        inDeg[y-1] += 1

    # 入力辺を持たない頂点をqueueに入れる
    d = deque()
    for v in range(N):
        if inDeg[v] == 0:
            d.append(v)

    # 各頂点の最初に入力辺を持たなかった点からの距離
    dp = [0] * N

    # トポロジカルオーダー t(v)の配列
    tList = [0] * N
    cnt = 0

    # For sequences, (strings, lists, tuples), use the fact that empty sequences are false.
    # https://www.python.org/dev/peps/pep-0008/#programming-recommendations
    while d:
        v = d.popleft()
        cnt += 1
        tList[v] = cnt
        for nv in graph[v]:
            # エッジ(v, nv)をグラフから削除する
            inDeg[nv] -= 1
            if inDeg[nv] == 0:
                # エッジがなくなったことで、入力辺がなくなったらqueueに入れる
                d.append(nv)
                # 最初に入力辺を持たなかった点からの距離
                dp[nv] = chmax(dp[nv], dp[v] + 1)

    # 出力
    # 最長経路
    print(max(dp))

    # トポロジカルオーダーの配列
    for i, t in enumerate(tList):
        print(i+1, t)  # 頂点v, トポロジカルオーダー t(v)


main()
