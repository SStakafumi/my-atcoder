import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


# N+1都市、M日以内
N, M = map(int, input().split())
D = [0] + [int(input()) for _ in range(N)]
C = [0] + [int(input()) for _ in range(M)]

# dp[i][j] = i番目の都市にj日目にいる時の最小疲労値の合計
INF = float('INF')
dp = [[INF]*(M+1) for _ in range(N+1)]
dp[0][1] = 0

for m in range(M+1):
    dp[0][m] = 0

for i in range(1, N+1):  # 1,2,....,N 個目の都市
    for j in range(1, M+1):  # 1,2,....,M+1 日
        # # もし日数jで都市i+1にいるのなら(1日目に都市2にいるとか)
        # if i == j:  # --- ①
        #     dp[i][j] = dp[i-1][j-1] + D[i]*C[j]
        # # もし日数jで都市iに行くことができたら
        # elif i < j+1:  # --- ②
        #     for k in range(i-1, j):
        #         dp[i][j] = min(dp[i-1][k]+D[i]*C[j], dp[i][j])

        # ①と②をまとめて
        if i <= j:
            for k in range(i-1, j):
                dp[i][j] = min(dp[i-1][k]+D[i]*C[j], dp[i][j])

print(min(dp[-1]))
