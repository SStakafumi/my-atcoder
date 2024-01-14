# DP[i][j] --- i番目の試行でカウンタがjのときの最大スコア(円)
N, M = map(int, input().split())
X = list(map(int, input().split()))

Y = [0] * (N+1)
for _ in range(M):
    c, y = map(int, input().split())
    Y[c] = y

dp = [[0] * (N+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(N):
        if j > i:
            break
        dp[i+1][j+1] = dp[i][j] + X[i] + Y[j+1]
        dp[i+1][0] = max(dp[i+1][0], dp[i][j])
        
        
print(max(dp[N]))