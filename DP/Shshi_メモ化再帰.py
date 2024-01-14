# メモ化再帰 -TLE-
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


N = int(input())
A = list(map(int, input().split()))

# dp[i][j][k] := 残り1個の皿がi枚、2個の皿がj枚、3個の皿がk枚の状態から、
# 寿司をすべてなくすのに必要な操作回数の期待値
# dpは0で初期化
dp = [[[0] * (N+1) for _ in range(N+1)] for _ in range(N+1)]


def f(i, j, k):
    if dp[i][j][k] != 0:
        # もしDP[c1][c2][c3]が埋まっていたらそれを返す
        return dp[i][j][k]
    if (i == 0 and j == 0 and k == 0):
        # 皿の上に寿司がない時は操作回数が0なので0.0を返す
        return 0.0

    fans = N * 1.0
    if i > 0:
        fans += f(i-1, j, k) * i
    if j > 0:
        fans += f(i+1, j-1, k) * j
    if k > 0:
        fans += f(i, j+1, k-1) * k
    fans *= 1.0 / (i + j + k)
    dp[i][j][k] = fans
    return dp[i][j][k]


c1, c2, c3 = [A.count(i+1) for i in range(3)]
print(f(c1, c2, c3))
