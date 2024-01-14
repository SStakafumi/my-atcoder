import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


D, N = map(int, input().split())
T = [0] + [int(input()) for _ in range(D)]

A = []
B = []
C = []
for j in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

INF = float('INF')

# dp[i][j] = i日目に服jを選んだときの最大スコア
dp = [[-INF]*N for _ in range(D+1)]

# i日目
for i in range(1, D+1):
    # i日目の気温
    t = T[i]
    # j番目の服を選ぶ時
    for j in range(N):
        # もしj番目の服が気温に適していたら
        if A[j] <= t <= B[j]:
            # もし初日だったらスコアは0
            if i == 1:
                dp[i][j] = 0
            # 初日じゃなかったら
            else:
                for k in range(N):
                    # dp[i][j] = max(i-1日目に服kを選んだ時の最大スコア＋服jと服kの派手さの差の絶対値, dp[i][j])
                    dp[i][j] = max(dp[i-1][k]+abs(C[j]-C[k]), dp[i][j])

print(max(dp[-1]))
