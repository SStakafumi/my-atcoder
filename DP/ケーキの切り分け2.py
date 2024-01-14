# ようわからんとりあえず飛ばす
import sys
def input(): return sys.stdin.readline().rstrip()


N = int(input())
A = [int(input()) for _ in range(N)]

# 要するに残りの状態からJOIくんの最大値は決まっている → それを利用しない手はない
# dp[i][j] = 残り区間[i,j]から始めた時のJOIくんの取り分の最大値

# 結局以下のようになる
# JOIくんのターンの時
# dp[i][j] = max(dp[i+1][j] + A[i],dp[i][j-1]+A[j])
# IOIちゃんのターンから始まる時
# dp[i][j] = dp[i+1][j] (A[i]>A[j])
# dp[i][j] = dp[i][j-1] (A[i]<A[j])

A += A

# dpは0からN-1行までしか考えない
dp = [[0]*(2*N) for _ in range(N)]

for w in range(1, N+1):  # 幅は1からNまで
    for i in range(N):  # 区間のはじめは0からN-1まで
        # Nと残り個数の偶奇が一致していたらJOIくんの番
        j = i+w
        if N % 2 == w % 2:
            if i != N-1:
                dp[i][j] = max(dp[i][j-1]+A[j-1], dp[i+1][j]+A[i])
            else:
                # i == N-1なら区間の始点をi+1からでなく0からと考える
                dp[i][j] = max(dp[0][j-1]+A[j-1], dp[0][w+1]+A[i])
        else:
            if A[i] < A[j-1]:
                dp[i][j] = dp[i][j-1]
            else:
                if i != N-1:
                    dp[i][j] = dp[i+1][j]
                else:
                    # i == N-1なら区間の始点をi+1からでなく0からと考える
                    dp[i][j] = dp[0][w+1]

ans = 0
for i in range(N):
    ans = max(dp[i][N+i], ans)

print(ans)
