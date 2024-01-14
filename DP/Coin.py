# コインは何枚でも選んでいい
# 1indexで解いている

n, m = map(int, input().split())
C = [0] + list(map(int, input().split()))

INF = float('INF')


# dp[i][j] = i枚目のコインまで選んだ時にj円になるようにした最小のコイン枚数
dp = [[INF]*(n+1) for _ in range(m+1)]
# 0枚目まで選んだ時に0円になる最小のコイン枚数は0枚
dp[0][0] = 0

for i in range(1, m+1):
    for j in range(n+1):
        if j - C[i] < 0:
            # 同列のC[i]前を参照できない時は一つ上
            dp[i][j] = dp[i-1][j]
        else:
            # そうでない時は同列C[i]前か、、一つ上の最小値を比較
            dp[i][j] = min(dp[i-1][j], 1+dp[i][j-C[i]])

print(dp[m][n])
