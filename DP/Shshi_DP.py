# PyPyであれば間に合う
import sys
# input処理を高速化する
input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))
    c1, c2, c3 = A.count(1), A.count(2), A.count(3)
    # dp[i][j][k] := 残り1個の皿がi枚、2個の皿がj枚、3個の皿がk枚の状態から、
    # 寿司をすべてなくすのに必要な操作回数の期待値
    dp = [[[0.0] * (N+1) for _ in range(N+1)] for _ in range(N+1)]
    # ここのforの流れはよくわからん
    for k in range(c3 + 1):
        for j in range(c2 + c3 + 1 - k):
            for i in range(c1 + c2 + c3 + 1 - k - j):
                if i == 0 and j == 0 and k == 0:
                    continue
                tmp = N * 1.0
                if i > 0:
                    tmp += i * dp[i - 1][j][k]
                if j > 0:
                    tmp += j * dp[i + 1][j - 1][k]
                if k > 0:
                    tmp += k * dp[i][j + 1][k - 1]
                dp[i][j][k] = tmp / (i + j + k)
    print(dp[c1][c2][c3])


main()
