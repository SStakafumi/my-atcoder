# pypyだとAC

import sys
input = sys.stdin.readline

n = int(input())
P = list(map(float, input().split()))

# dp[i][j] = i枚目のコインまで投げた時、表がj枚出る確率
dp = [[0]*(n+1) for _ in range(n)]

# 一枚目
dp[0][0] = 1-P[0]
dp[0][1] = P[0]

# 2枚目以降
for i in range(1, n):
    for j in range(n+1):
        # dp[i][j] = (i−1枚目のコインまで投げたとき、表がj枚でる確率)×(i枚目のコインが裏である確率)
        # +(i−1枚目のコインまで投げたとき、表がj−1枚でる確率)×(i枚目のコインが表である確率)
        dp[i][j] = dp[i-1][j] * (1-P[i]) + dp[i-1][j-1] * P[i]

ans = sum(dp[n-1][(n+1)//2:])
print(ans)
