import sys


def input():
    # 入力速度を上げる
    return sys.stdin.readline().rstrip()


N, W = map(int, input().split())  # 品数, コスト制限

weightList = []
valueList = []
for i in range(N):
    w, v = map(int, input().split())
    weightList.append(w)
    valueList.append(v)

INF = float('INF')
maxValue = 100010  # 最大価値は高々 100 * 1000 +10

# dp[i][j] = i番目の品を考えた時価値がjになるような最小コスト
dp = [[INF]*maxValue for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(maxValue):
        notChoiceCost = dp[i][j]
        if j >= valueList[i]:
            choiceCost = dp[i][j - valueList[i]] + weightList[i]
            if choiceCost < dp[i+1][j]:
                dp[i+1][j] = choiceCost
        if notChoiceCost < dp[i+1][j]:
            dp[i+1][j] = notChoiceCost

ans = 0
for j in range(maxValue):
    if dp[N][j] <= W:
        ans = j

print(ans)
