N, K = map(int, input().split())
H = [0] + list(map(int, input().split()))

dp = [0]*(N+1)
dp[1] = 0
INF = float('INF')  # INFを使う時はこうしてから使ったほうが良い

for i in range(2, N+1):
    tmp = INF
    for j in range(1, K+1):
        if i-j < 1:
            continue
        tmp = min(tmp, dp[i-j]+abs(H[i-j]-H[i]))
    dp[i] = tmp

print(dp[N])
